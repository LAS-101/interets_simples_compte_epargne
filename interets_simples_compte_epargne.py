"""
Intérêts Simples - Applications pour un Compte d'Épargne
Simple Interest - Savings Account Applications

Ce programme calcule les intérêts simples pour différents scénarios de compte d'épargne.
This program calculates simple interest for various savings account scenarios.
"""

def calculer_interet_simple(principal, taux, duree):
    """
    Calcule l'intérêt simple.
    
    Formule: I = P *r *t
    où:
        I = Intérêt (Interest)
        P = Principal (Capital initial)
        r = Taux d'intérêt annuel (Annual interest rate, en décimal)
        t = Durée (Time period in years)
    
    Args:
        principal (float): Montant initial déposé
        taux (float): Taux d'intérêt annuel (en pourcentage)
        duree (float): Durée en années
    
    Returns:
        float: Montant des intérêts
    """
    taux_decimal = taux / 100
    interet = principal * taux_decimal * duree
    return interet


def calculer_montant_total(principal, taux, duree):
    """
    Calcule le montant total (capital + intérêts).
    
    Formule: A = P + I = P(1 + rt)
    
    Args:
        principal (float): Montant initial
        taux (float): Taux d'intérêt annuel (en pourcentage)
        duree (float): Durée en années
    
    Returns:
        float: Montant total
    """
    interet = calculer_interet_simple(principal, taux, duree)
    montant_total = principal + interet
    return montant_total


def calculer_duree_necessaire(principal, montant_cible, taux):
    """
    Calcule la durée nécessaire pour atteindre un montant cible.
    
    Formule: t = (A - P) / (P × r)
    
    Args:
        principal (float): Montant initial
        montant_cible (float): Montant que vous souhaitez atteindre
        taux (float): Taux d'intérêt annuel (en pourcentage)
    
    Returns:
        float: Durée en années
    """
    taux_decimal = taux / 100
    duree = (montant_cible - principal) / (principal * taux_decimal)
    return duree


def calculer_taux_necessaire(principal, montant_cible, duree):
    """
    Calcule le taux d'intérêt nécessaire pour atteindre un montant cible.
    
    Formule: r = (A - P) / (P*t)
    
    Args:
        principal (float): Montant initial
        montant_cible (float): Montant que vous souhaitez atteindre
        duree (float): Durée en années
    
    Returns:
        float: Taux d'intérêt annuel (en pourcentage)
    """
    taux_decimal = (montant_cible - principal) / (principal * duree)
    taux_pourcentage = taux_decimal * 100
    return taux_pourcentage


def calculer_principal_necessaire(montant_cible, taux, duree):
    """
    Calcule le capital initial nécessaire pour atteindre un montant cible.
    
    Formule: P = A / (1 + rt)
    
    Args:
        montant_cible (float): Montant que vous souhaitez atteindre
        taux (float): Taux d'intérêt annuel (en pourcentage)
        duree (float): Durée en années
    
    Returns:
        float: Capital initial nécessaire
    """
    taux_decimal = taux / 100
    principal = montant_cible / (1 + taux_decimal * duree)
    return principal


def afficher_tableau_evolution(principal, taux, duree_max):
    """
    Affiche un tableau d'évolution du compte d'épargne année par année.
    
    Args:
        principal (float): Montant initial
        taux (float): Taux d'intérêt annuel (en pourcentage)
        duree_max (int): Nombre d'années à afficher
    """
    print("\n" + "="*70)
    print(f"ÉVOLUTION DU COMPTE D'ÉPARGNE")
    print(f"Capital initial: {principal:,.2f} €")
    print(f"Taux d'intérêt: {taux}% par an")
    print("="*70)
    print(f"{'Année':<8} {'Intérêts':<15} {'Total':<15} {'Gain total':<15}")
    print("-"*70)
    
    for annee in range(1, duree_max + 1):
        interet = calculer_interet_simple(principal, taux, annee)
        total = principal + interet
        print(f"{annee:<8} {interet:>12,.2f} € {total:>12,.2f} € {interet:>12,.2f} €")
    
    print("="*70)


def comparer_comptes(principal, liste_taux, duree):
    """
    Compare différents comptes d'épargne avec différents taux d'intérêt.
    
    Args:
        principal (float): Montant initial
        liste_taux (list): Liste de taux d'intérêt à comparer
        duree (float): Durée en années
    """
    print("\n" + "="*70)
    print(f"COMPARAISON DE COMPTES D'ÉPARGNE")
    print(f"Capital initial: {principal:,.2f} €")
    print(f"Durée: {duree} ans")
    print("="*70)
    print(f"{'Taux':<10} {'Intérêts':<15} {'Montant final':<15}")
    print("-"*70)
    
    for taux in liste_taux:
        interet = calculer_interet_simple(principal, taux, duree)
        total = principal + interet
        print(f"{taux}%{'':<7} {interet:>12,.2f} € {total:>12,.2f} €")
    
    print("="*70)


def menu_principal():
    """
    Menu interactif pour utiliser les différentes fonctions.
    """
    while True:
        print("\n" + "="*70)
        print("CALCULATEUR D'INTÉRÊTS SIMPLES - COMPTE D'ÉPARGNE")
        print("="*70)
        print("1. Calculer les intérêts et le montant total")
        print("2. Calculer la durée nécessaire pour atteindre un objectif")
        print("3. Calculer le taux nécessaire pour atteindre un objectif")
        print("4. Calculer le capital initial nécessaire")
        print("5. Voir le tableau d'évolution année par année")
        print("6. Comparer différents taux d'intérêt")
        print("7. Exemples pratiques")
        print("0. Quitter")
        print("="*70)
        
        choix = input("\nChoisissez une option (0-7): ")
        
        if choix == "1":
            print("\n--- CALCUL DES INTÉRÊTS ---")
            principal = float(input("Montant initial (€): "))
            taux = float(input("Taux d'intérêt annuel (%): "))
            duree = float(input("Durée (années): "))
            
            interet = calculer_interet_simple(principal, taux, duree)
            total = calculer_montant_total(principal, taux, duree)
            
            print(f"\n✓ Intérêts gagnés: {interet:,.2f} €")
            print(f"✓ Montant total: {total:,.2f} €")
        
        elif choix == "2":
            print("\n--- DURÉE NÉCESSAIRE ---")
            principal = float(input("Montant initial (€): "))
            montant_cible = float(input("Montant cible (€): "))
            taux = float(input("Taux d'intérêt annuel (%): "))
            
            duree = calculer_duree_necessaire(principal, montant_cible, taux)
            
            print(f"\n✓ Durée nécessaire: {duree:.2f} ans")
            print(f"  (soit environ {int(duree * 12)} mois)")
        
        elif choix == "3":
            print("\n--- TAUX NÉCESSAIRE ---")
            principal = float(input("Montant initial (€): "))
            montant_cible = float(input("Montant cible (€): "))
            duree = float(input("Durée (années): "))
            
            taux = calculer_taux_necessaire(principal, montant_cible, duree)
            
            print(f"\n✓ Taux nécessaire: {taux:.2f}% par an")
        
        elif choix == "4":
            print("\n--- CAPITAL INITIAL NÉCESSAIRE ---")
            montant_cible = float(input("Montant cible (€): "))
            taux = float(input("Taux d'intérêt annuel (%): "))
            duree = float(input("Durée (années): "))
            
            principal = calculer_principal_necessaire(montant_cible, taux, duree)
            
            print(f"\n✓ Capital initial nécessaire: {principal:,.2f} €")
        
        elif choix == "5":
            print("\n--- TABLEAU D'ÉVOLUTION ---")
            principal = float(input("Montant initial (€): "))
            taux = float(input("Taux d'intérêt annuel (%): "))
            duree_max = int(input("Nombre d'années à afficher: "))
            
            afficher_tableau_evolution(principal, taux, duree_max)
        
        elif choix == "6":
            print("\n--- COMPARAISON DE TAUX ---")
            principal = float(input("Montant initial (€): "))
            duree = float(input("Durée (années): "))
            nb_taux = int(input("Combien de taux voulez-vous comparer? "))
            
            liste_taux = []
            for i in range(nb_taux):
                taux = float(input(f"Taux {i+1} (%): "))
                liste_taux.append(taux)
            
            comparer_comptes(principal, liste_taux, duree)
        
        elif choix == "7":
            exemples_pratiques()
        
        elif choix == "0":
            print("\nMerci d'avoir utilisé le calculateur d'intérêts simples!")
            break
        
        else:
            print("\n⚠ Option invalide. Veuillez choisir entre 0 et 7.")


def exemples_pratiques():
    """
    Affiche des exemples pratiques d'utilisation.
    """
    print("\n" + "="*70)
    print("EXEMPLES PRATIQUES")
    print("="*70)
    
    # Exemple 1
    print("\n EXEMPLE 1: Épargne pour les vacances")
    print("-" * 70)
    principal = 5000
    taux = 2.5
    duree = 2
    interet = calculer_interet_simple(principal, taux, duree)
    total = calculer_montant_total(principal, taux, duree)
    print(f"Vous déposez {principal:,.2f} € à {taux}% pendant {duree} ans")
    print(f"→ Intérêts gagnés: {interet:,.2f} €")
    print(f"→ Montant total: {total:,.2f} €")
    
    # Exemple 2
    print("\n EXEMPLE 2: Épargne pour l'université")
    print("-" * 70)
    principal = 10000
    taux = 3.0
    duree = 5
    interet = calculer_interet_simple(principal, taux, duree)
    total = calculer_montant_total(principal, taux, duree)
    print(f"Vous déposez {principal:,.2f} € à {taux}% pendant {duree} ans")
    print(f"→ Intérêts gagnés: {interet:,.2f} €")
    print(f"→ Montant total: {total:,.2f} €")
    
    # Exemple 3
    print("\n EXEMPLE 3: Combien de temps pour doubler son argent?")
    print("-" * 70)
    principal = 1000
    montant_cible = 2000
    taux = 4.0
    duree = calculer_duree_necessaire(principal, montant_cible, taux)
    print(f"Pour doubler {principal:,.2f} € avec un taux de {taux}%")
    print(f"→ Il faut: {duree:.1f} ans (soit {int(duree * 12)} mois)")
    
    # Exemple 4
    print("\n EXEMPLE 4: Quel taux pour atteindre un objectif?")
    print("-" * 70)
    principal = 8000
    montant_cible = 10000
    duree = 3
    taux = calculer_taux_necessaire(principal, montant_cible, duree)
    print(f"Pour transformer {principal:,.2f} € en {montant_cible:,.2f} € en {duree} ans")
    print(f"→ Taux nécessaire: {taux:.2f}% par an")
    
    # Exemple 5: Comparaison
    print("\n EXEMPLE 5: Comparaison de différents comptes")
    print("-" * 70)
    comparer_comptes(5000, [1.5, 2.0, 2.5, 3.0], 3)
    
    print("\n" + "="*70)


# Programme principal
if __name__ == "__main__":
    print("\n" + "="*70)
    print("BIENVENUE DANS LE CALCULATEUR D'INTÉRÊTS SIMPLES")
    print("="*70)
    print("\nCe programme vous aide à comprendre et calculer les intérêts simples")
    print("pour vos comptes d'épargne.")
    
    # Afficher d'abord les exemples
    exemples_pratiques()
    
    # Puis proposer le menu interactif
    input("\nAppuyez sur Entrée pour accéder au menu interactif...")
    menu_principal()