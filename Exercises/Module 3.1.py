def pH2Category(pH):
    if pH < 3 and pH > 0 :
        category = "Strongly acidic"
    elif pH < 6 and pH >= 3 :
        category = "Weakly acidic"
    elif pH < 8 and pH >=6 :
        category = "Neutral"
    elif pH < 11 and pH >=8 :
        category = "Weakly basic"
    elif pH < 14 and pH >= 11 :
        category = "Strongly basic"
    else:
        category = "pH out of range"
    return category

