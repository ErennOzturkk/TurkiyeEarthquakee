import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
import json

# Sayfa yapılandırması
st.set_page_config(
    page_title="Türkiye Deprem Risk Haritası V3",
    page_icon="🗺️",
    layout="wide"
)

# Başlık
st.title("🗺️ Türkiye İl Bazlı Deprem Risk Analizi - Model V3")
st.markdown("---")

# GeoJSON dosyasını yükle
@st.cache_data
def load_geojson():
    try:
        gdf = gpd.read_file("TURKIYE_IL_BAZLI_RISK_ANALIZI_V3.geojson")
        return gdf
    except Exception as e:
        st.error(f"GeoJSON dosyası yüklenirken hata oluştu: {e}")
        return None

# Veriyi yükle
gdf = load_geojson()

if gdf is not None:
    # Sidebar - Bilgi paneli
    with st.sidebar:
        st.header("📊 Harita Bilgileri")
        st.markdown("""
        **Model V3 Özellikleri:**
        - Risk = %50 Toplam Tehlike + %50 Kırılganlık
        - Toplam Tehlike = %70 Fay + %30 Tarihsel (Büyüklük Toplamı)
        - 50km etki alanı dikkate alınmıştır
        """)
        
        st.markdown("---")
        st.subheader("🎯 Kullanım")
        st.markdown("""
        Haritada bir ile tıklayarak
        o ile ait detaylı risk
        bilgilerini görebilirsiniz.
        """)
        
        st.markdown("---")
        st.subheader("📈 Risk Skoru")
        st.markdown("""
        Risk skoru **1-10** arasındadır:
        - **1-3**: Düşük Risk
        - **4-6**: Orta Risk  
        - **7-8**: Yüksek Risk
        - **9-10**: Çok Yüksek Risk
        """)
    
    # İl seçimi için dropdown
    il_listesi = sorted(gdf['name'].tolist())
    selected_il_name = st.selectbox(
        "🔍 İl Seçin (veya haritaya tıklayın):",
        ["Haritadan seçin..."] + il_listesi,
        key="il_selector"
    )
    
    # Ana harita
    st.subheader("📍 İnteraktif Risk Haritası")
    
    # Folium haritası oluştur
    m = folium.Map(
        location=[39.0, 35.0],
        zoom_start=6,
        tiles='OpenStreetMap'
    )
    
    def get_color(risk_score):
        """Risk skoruna göre renk döndür"""
        if risk_score <= 3:
            return 'green'
        elif risk_score <= 6:
            return 'orange'
        elif risk_score <= 8:
            return 'red'
        else:
            return 'darkred'
    
    # Her il için popup ve tooltip ekle
    for idx, row in gdf.iterrows():
        # Popup içeriği
        popup_html = f"""
        <div style="font-family: Arial; width: 250px;">
            <h3 style="margin: 0; color: #333;">{row['name']}</h3>
            <hr style="margin: 5px 0;">
            <p style="margin: 5px 0;"><b>Risk Skoru:</b> {row['RISK_SKORU_10']:.2f}/10</p>
            <p style="margin: 5px 0;"><b>Toplam Tehlike:</b> {row['Puan_Tehlike_TOPLAM']:.3f}</p>
            <p style="margin: 5px 0;"><b>Kırılganlık:</b> {row['Puan_Kirilganlik']:.3f}</p>
            <p style="margin: 5px 0;"><b>Nüfus:</b> {row['ToplamNufus']:,.0f}</p>
            <p style="margin: 5px 0; font-size: 10px; color: #666;">Detaylar için haritaya tıklayın</p>
        </div>
        """
        
        # Tooltip
        tooltip_text = f"{row['name']} - Risk: {row['RISK_SKORU_10']:.2f}"
        
        # GeoJSON feature ekle
        folium.GeoJson(
            row.geometry,
            style_function=lambda feature, risk=row['RISK_SKORU_10']: {
                'fillColor': get_color(risk),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.6,
            },
            tooltip=tooltip_text,
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)
    
    # Haritayı göster ve tıklama olayını yakala
    map_data = st_folium(m, width=1200, height=700, returned_objects=["last_object_clicked"])
    
    # Tıklanan il bilgisini al
    selected_il = None
    
    # Dropdown'dan seçim yapıldıysa
    if selected_il_name and selected_il_name != "Haritadan seçin...":
        selected_il = gdf[gdf['name'] == selected_il_name].iloc[0]
    # Haritaya tıklama olayı
    elif map_data["last_object_clicked"]:
        clicked_lat = map_data["last_object_clicked"]["lat"]
        clicked_lon = map_data["last_object_clicked"]["lng"]
        
        # Tıklanan noktanın hangi il içinde olduğunu bul
        from shapely.geometry import Point
        clicked_point = Point(clicked_lon, clicked_lat)
        
        for idx, row in gdf.iterrows():
            if row.geometry.contains(clicked_point):
                selected_il = row
                break
    
    # Eğer il seçildiyse detayları göster
    if selected_il is not None:
            
            st.markdown("---")
            st.subheader(f"📋 {selected_il['name']} İli - Detaylı Risk Analizi")
            
            # İki sütunlu layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🎯 Risk Skorları")
                st.metric("Risk Skoru (1-10)", f"{selected_il['RISK_SKORU_10']:.2f}")
                
                # Risk seviyesi
                risk_score = selected_il['RISK_SKORU_10']
                if risk_score <= 3:
                    risk_level = "🟢 Düşük Risk"
                    risk_color = "green"
                elif risk_score <= 6:
                    risk_level = "🟡 Orta Risk"
                    risk_color = "orange"
                elif risk_score <= 8:
                    risk_level = "🟠 Yüksek Risk"
                    risk_color = "red"
                else:
                    risk_level = "🔴 Çok Yüksek Risk"
                    risk_color = "darkred"
                
                st.markdown(f"**Risk Seviyesi:** {risk_level}")
                
                st.markdown("### 📊 Tehlike Puanları")
                st.metric("Toplam Tehlike", f"{selected_il['Puan_Tehlike_TOPLAM']:.3f}")
                st.metric("Fay Tehlike", f"{selected_il['Puan_Tehlike_FAY']:.3f}")
                st.metric("Tarihsel Tehlike", f"{selected_il['Puan_Tehlike_TARIHSEL']:.3f}")
            
            with col2:
                st.markdown("### 🏗️ Kırılganlık Bilgileri")
                st.metric("Kırılganlık Puanı", f"{selected_il['Puan_Kirilganlik']:.3f}")
                st.metric("Eski Hane Oranı", f"{selected_il['Eski_Hane_Orani']:.2%}")
                
                st.markdown("### 👥 Demografik Bilgiler")
                st.metric("Toplam Nüfus", f"{selected_il['ToplamNufus']:,.0f}")
                
                st.markdown("### 📈 Detaylı Metrikler")
                st.metric("Fay Tehlike Oranı", f"{selected_il['Fay_Tehlike_Orani']:.4f}")
                st.metric("Tarihsel Puan (Toplam Mag)", f"{selected_il['Tarihsel_Puan_Toplam_Mag']:.1f}")
            
            # Açıklama
            st.markdown("---")
            st.markdown("### 📝 Açıklamalar")
            st.info(f"""
            **{selected_il['name']}** ili için:
            - **Risk Skoru**: {selected_il['RISK_SKORU_10']:.2f}/10
            - **Toplam Tehlike Puanı**: {selected_il['Puan_Tehlike_TOPLAM']:.3f} (Fay: %{selected_il['Puan_Tehlike_FAY']*100:.1f}, Tarihsel: %{selected_il['Puan_Tehlike_TARIHSEL']*100:.1f})
            - **Kırılganlık Puanı**: {selected_il['Puan_Kirilganlik']:.3f} (Eski bina oranı: {selected_il['Eski_Hane_Orani']:.1%})
            - **Nüfus**: {selected_il['ToplamNufus']:,.0f} kişi
            """)
    else:
        st.info("👆 Haritada bir ile tıklayarak detaylı bilgileri görebilirsiniz.")
    
    # En riskli 10 il tablosu
    st.markdown("---")
    st.subheader("🏆 En Riskli 10 İl")
    
    top_10 = gdf.nlargest(10, "RISK_SKORU_10")[["name", "RISK_SKORU_10", "Puan_Tehlike_TOPLAM", "Puan_Kirilganlik"]]
    top_10 = top_10.rename(columns={
        "name": "İl Adı",
        "RISK_SKORU_10": "Risk Skoru",
        "Puan_Tehlike_TOPLAM": "Toplam Tehlike",
        "Puan_Kirilganlik": "Kırılganlık"
    })
    top_10["Risk Skoru"] = top_10["Risk Skoru"].round(2)
    top_10["Toplam Tehlike"] = top_10["Toplam Tehlike"].round(3)
    top_10["Kırılganlık"] = top_10["Kırılganlık"].round(3)
    
    st.dataframe(top_10, use_container_width=True, hide_index=True)
    
else:
    st.error("GeoJSON dosyası yüklenemedi. Lütfen 'TURKIYE_IL_BAZLI_RISK_ANALIZI_V3.geojson' dosyasının mevcut olduğundan emin olun.")

