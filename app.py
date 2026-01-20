import streamlit as st
from core.calculator import PricingCalculator

st.set_page_config(page_title="Facturation BTTF", page_icon="💳")

st.title("🎬 Système de Facturation BTTF")
st.markdown("Solution professionnelle pour la gestion des promotions DVD.")

# Zone de saisie
st.subheader("🛒 Panier Client")
input_data = st.text_area(
    "Entrez les titres des films (un par ligne) :",
    height=200,
    placeholder="Back to the Future 1\nBack to the Future 2\nLa chèvre",
    key="cart_input"
)

# Bouton de calcul
if st.button("CALCULER LE TOTAL", use_container_width=True):
    if input_data.strip():
        total = PricingCalculator.calculate_total(input_data)
        st.balloons()
        st.success(f"### Montant Total à Facturer : {total} €")
    else:
        st.warning("Le panier est vide.")