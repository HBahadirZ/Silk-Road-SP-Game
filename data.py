# data.py

from caravan_management import Member

goods = {
    "Silk": {
        "base_value": 100,
        "rarity": 5
    },
    "Spices": {
        "base_value": 150,
        "rarity": 4
    },
    "Tea": {
        "base_value": 80,
        "rarity": 3
    },
    "Porcelain": {
        "base_value": 120,
        "rarity": 4
    },
    "Precious Gems": {
        "base_value": 300,
        "rarity": 6
    },
    "Gold and Silver": {
        "base_value": 250,
        "rarity": 5
    },
    "Textiles": {
        "base_value": 70,
        "rarity": 2
    },
    "Paper": {
        "base_value": 50,
        "rarity": 2
    },
    "Ivory": {
        "base_value": 200,
        "rarity": 5
    },
    "Glassware": {
        "base_value": 110,
        "rarity": 3
    },
    "Perfumes and Incense": {
        "base_value": 130,
        "rarity": 4
    },
    "Horses": {
        "base_value": 220,
        "rarity": 5
    },
    "Exotic Animals": {
        "base_value": 400,
        "rarity": 6
    },
    "Carpets and Rugs": {
        "base_value": 160,
        "rarity": 3
    },
    "Dyes": {
        "base_value": 90,
        "rarity": 3
    },
}

markets = {
    "Chang'an (Xi'an)": {
        "Silk": 1.5,
        "Spices": 0.8,
        "Tea": 1.2,
        "Porcelain": 1.1,
        "Precious Gems": 0.9,
        "Gold and Silver": 1.0,
        "Textiles": 1.3,
        "Paper": 1.4,
        "Ivory": 0.7,
        "Glassware": 1.2,
        "Perfumes and Incense": 0.9,
        "Horses": 1.0,
        "Exotic Animals": 0.5,
        "Carpets and Rugs": 0.8,
        "Dyes": 1.1
    },
    "Samarkand": {
        "Silk": 1.2,
        "Spices": 1.3,
        "Tea": 1.0,
        "Porcelain": 1.0,
        "Precious Gems": 1.5,
        "Gold and Silver": 1.1,
        "Textiles": 0.9,
        "Paper": 0.8,
        "Ivory": 1.2,
        "Glassware": 0.9,
        "Perfumes and Incense": 1.3,
        "Horses": 1.4,
        "Exotic Animals": 0.7,
        "Carpets and Rugs": 1.1,
        "Dyes": 1.2
    },
    "Bukhara": {
        "Silk": 1.3,
        "Spices": 1.1,
        "Tea": 0.9,
        "Porcelain": 1.2,
        "Precious Gems": 1.4,
        "Gold and Silver": 1.0,
        "Textiles": 1.0,
        "Paper": 0.7,
        "Ivory": 1.1,
        "Glassware": 1.0,
        "Perfumes and Incense": 1.2,
        "Horses": 1.3,
        "Exotic Animals": 0.6,
        "Carpets and Rugs": 1.0,
        "Dyes": 1.3
    },
    "Kashgar": {
        "Silk": 1.4,
        "Spices": 1.2,
        "Tea": 1.1,
        "Porcelain": 1.3,
        "Precious Gems": 1.6,
        "Gold and Silver": 1.2,
        "Textiles": 1.1,
        "Paper": 0.9,
        "Ivory": 1.3,
        "Glassware": 1.1,
        "Perfumes and Incense": 1.4,
        "Horses": 1.5,
        "Exotic Animals": 0.8,
        "Carpets and Rugs": 1.3,
        "Dyes": 1.5
    },
    "Constantinople (Istanbul)": {
        "Silk": 1.6,
        "Spices": 1.5,
        "Tea": 1.3,
        "Porcelain": 1.4,
        "Precious Gems": 1.7,
        "Gold and Silver": 1.3,
        "Textiles": 1.4,
        "Paper": 1.2,
        "Ivory": 1.5,
        "Glassware": 1.3,
        "Perfumes and Incense": 1.5,
        "Horses": 1.6,
        "Exotic Animals": 1.0,
        "Carpets and Rugs": 1.5,
        "Dyes": 1.6
    },
    "Baghdad": {
        "Silk": 1.5,
        "Spices": 1.4,
        "Tea": 1.2,
        "Porcelain": 1.3,
        "Precious Gems": 1.6,
        "Gold and Silver": 1.2,
        "Textiles": 1.3,
        "Paper": 1.1,
        "Ivory": 1.4,
        "Glassware": 1.2,
        "Perfumes and Incense": 1.4,
        "Horses": 1.5,
        "Exotic Animals": 0.9,
        "Carpets and Rugs": 1.4,
        "Dyes": 1.5
    },
    "Aleppo": {
        "Silk": 1.4,
        "Spices": 1.3,
        "Tea": 1.1,
        "Porcelain": 1.2,
        "Precious Gems": 1.5,
        "Gold and Silver": 1.1,
        "Textiles": 1.2,
        "Paper": 1.0,
        "Ivory": 1.3,
        "Glassware": 1.1,
        "Perfumes and Incense": 1.3,
        "Horses": 1.4,
        "Exotic Animals": 0.8,
        "Carpets and Rugs": 1.3,
        "Dyes": 1.4
    },
    "Damascus": {
        "Silk": 1.3,
        "Spices": 1.2,
        "Tea": 1.0,
        "Porcelain": 1.1,
        "Precious Gems": 1.4,
        "Gold and Silver": 1.0,
        "Textiles": 1.1,
        "Paper": 0.9,
        "Ivory": 1.2,
        "Glassware": 1.0,
        "Perfumes and Incense": 1.2,
        "Horses": 1.3,
        "Exotic Animals": 0.7,
        "Carpets and Rugs": 1.2,
        "Dyes": 1.3
    },
    "Tehran": {
        "Silk": 1.2,
        "Spices": 1.1,
        "Tea": 0.9,
        "Porcelain": 1.0,
        "Precious Gems": 1.3,
        "Gold and Silver": 0.9,
        "Textiles": 1.0,
        "Paper": 0.8,
        "Ivory": 1.1,
        "Glassware": 0.9,
        "Perfumes and Incense": 1.1,
        "Horses": 1.2,
        "Exotic Animals": 0.6,
        "Carpets and Rugs": 1.1,
        "Dyes": 1.2
    },
    "Merv": {
        "Silk": 1.1,
        "Spices": 1.0,
        "Tea": 0.8,
        "Porcelain": 0.9,
        "Precious Gems": 1.2,
        "Gold and Silver": 0.8,
        "Textiles": 0.9,
        "Paper": 0.7,
        "Ivory": 1.0,
        "Glassware": 0.8,
        "Perfumes and Incense": 1.0,
        "Horses": 1.1,
        "Exotic Animals": 0.5,
        "Carpets and Rugs": 1.0,
        "Dyes": 1.1
    },
    "Herat": {
        "Silk": 1.0,
        "Spices": 0.9,
        "Tea": 0.7,
        "Porcelain": 0.8,
        "Precious Gems": 1.1,
        "Gold and Silver": 0.7,
        "Textiles": 0.8,
        "Paper": 0.6,
        "Ivory": 0.9,
        "Glassware": 0.7,
        "Perfumes and Incense": 0.9,
        "Horses": 1.0,
        "Exotic Animals": 0.4,
        "Carpets and Rugs": 0.9,
        "Dyes": 1.0
    },
    "Khotan": {
        "Silk": 1.3,
        "Spices": 1.2,
        "Tea": 1.0,
        "Porcelain": 1.1,
        "Precious Gems": 1.4,
        "Gold and Silver": 1.1,
        "Textiles": 1.2,
        "Paper": 0.8,
        "Ivory": 1.3,
        "Glassware": 1.0,
        "Perfumes and Incense": 1.2,
        "Horses": 1.4,
        "Exotic Animals": 0.7,
        "Carpets and Rugs": 1.2,
        "Dyes": 1.3
    },
    "Antioch": {
        "Silk": 1.4,
        "Spices": 1.3,
        "Tea": 1.1,
        "Porcelain": 1.2,
        "Precious Gems": 1.5,
        "Gold and Silver": 1.2,
        "Textiles": 1.3,
        "Paper": 0.9,
        "Ivory": 1.4,
        "Glassware": 1.1,
        "Perfumes and Incense": 1.3,
        "Horses": 1.5,
        "Exotic Animals": 0.8,
        "Carpets and Rugs": 1.3,
        "Dyes": 1.4
    },
    "Sarai": {
        "Silk": 1.2,
        "Spices": 1.1,
        "Tea": 0.9,
        "Porcelain": 1.0,
        "Precious Gems": 1.3,
        "Gold and Silver": 1.0,
        "Textiles": 1.1,
        "Paper": 0.7,
        "Ivory": 1.2,
        "Glassware": 0.9,
        "Perfumes and Incense": 1.1,
        "Horses": 1.3,
        "Exotic Animals": 0.6,
        "Carpets and Rugs": 1.2,
        "Dyes": 1.3
    },
    "Venice": {
        "Silk": 1.5,
        "Spices": 1.4,
        "Tea": 1.3,
        "Porcelain": 1.4,
        "Precious Gems": 1.6,
        "Gold and Silver": 1.3,
        "Textiles": 1.4,
        "Paper": 1.1,
        "Ivory": 1.5,
        "Glassware": 1.3,
        "Perfumes and Incense": 1.4,
        "Horses": 1.6,
        "Exotic Animals": 0.9,
        "Carpets and Rugs": 1.5,
        "Dyes": 1.6
    },
}

potential_members = [
    Member(name="Aldric",
           role="Guard",
           health=100,
           skill_level=5,
           upfront_fee=100,
           wage=20,
           food_consumption=3,
           water_consumption=2,
           morale=100),
    Member(name="Branwen",
           role="Merchant",
           health=100,
           skill_level=4,
           upfront_fee=80,
           wage=16,
           food_consumption=2,
           water_consumption=1,
           morale=100),
    Member(name="Caelan",
           role="Scout",
           health=100,
           skill_level=3,
           upfront_fee=60,
           wage=12,
           food_consumption=2,
           water_consumption=3,
           morale=100),
    Member(name="Deryn",
           role="Healer",
           health=100,
           skill_level=5,
           upfront_fee=100,
           wage=20,
           food_consumption=2,
           water_consumption=2,
           morale=100),
    Member(name="Eldric",
           role="Guard",
           health=100,
           skill_level=8,
           upfront_fee=160,
           wage=32,
           food_consumption=4,
           water_consumption=3,
           morale=100),
    Member(name="Faelan",
           role="Merchant",
           health=100,
           skill_level=6,
           upfront_fee=120,
           wage=24,
           food_consumption=3,
           water_consumption=2,
           morale=100),
    Member(name="Gareth",
           role="Scout",
           health=100,
           skill_level=7,
           upfront_fee=140,
           wage=28,
           food_consumption=3,
           water_consumption=4,
           morale=100),
    Member(name="Halwyn",
           role="Healer",
           health=100,
           skill_level=9,
           upfront_fee=180,
           wage=36,
           food_consumption=3,
           water_consumption=3,
           morale=100),
    Member(name="Ivor",
           role="Guard",
           health=100,
           skill_level=7,
           upfront_fee=140,
           wage=28,
           food_consumption=3,
           water_consumption=3,
           morale=100),
    Member(name="Jareth",
           role="Merchant",
           health=100,
           skill_level=8,
           upfront_fee=160,
           wage=32,
           food_consumption=3,
           water_consumption=2,
           morale=100)
]
