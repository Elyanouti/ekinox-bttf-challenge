class PricingCalculator:
    """Gère le calcul des prix et des promotions pour la boutique de DVD."""
    
    UNIT_PRICE_BTTF = 15.0
    UNIT_PRICE_OTHER = 20.0
    BTTF_KEYWORD = "Back to the Future"

    @classmethod
    def calculate_total(cls, cart_text: str) -> float:
        """Analyse le texte du panier et retourne le prix total TTC."""
        if not cart_text or not cart_text.strip():
            return 0.0

        # Nettoyage des données d'entrée
        lines = [line.strip() for line in cart_text.split('\n') if line.strip()]
        
        bttf_items = [m for m in lines if cls.BTTF_KEYWORD in m]
        other_items_count = len(lines) - len(bttf_items)

        # Calcul de la remise selon le nombre de volets différents
        # On utilise set() pour compter uniquement les titres uniques
        unique_parts_count = len(set(bttf_items))
        
        discount_rate = 0.0
        if unique_parts_count == 2:
            discount_rate = 0.10  # -10%
        elif unique_parts_count >= 3:
            discount_rate = 0.20  # -20%

        # Calcul final
        total_bttf = len(bttf_items) * cls.UNIT_PRICE_BTTF * (1 - discount_rate)
        total_others = other_items_count * cls.UNIT_PRICE_OTHER
        
        return round(total_bttf + total_others, 2)