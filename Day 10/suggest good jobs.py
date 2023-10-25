skills = {
    "marketing_strategy" : {
        "mathematics": 4,
        "team_work": 4,
        "creative_activities": 4,
        "understanding_human_behavior": 3
    },

    "market_research" : {
        "mathematics": 5,
        "team_work": 2,
        "creative_activities": 3,
        "understanding_human_behavior": 3
    },

    "digital_marketing" : {
        "mathematics": 3,
        "team_work": 1,
        "creative_activities": 2,
        "understanding_human_behavior": 1
    }
}

userKnowledge = {
    "mathematics": 4,
    "team_work": 4,
    "creative_activities": 4,
    "understanding_human_behavior": 3
}

user_skill = []

for skill in skills.keys():
    count = 0
    for skill_needs in skill.keys():
        if(skill[skill_needs] <= userKnowledge[skill_needs]):
            count += 1
    if count == 4:
        user_skill.append(skill)

suggest = []
jobs = {
    {
        "name":"Account Manager",
        "list":["market_research", "digital_marketing"]
    },
    {
        "name":"Assistant",
        "list":["digital_marketing"]
    }
    
}

user_skill.sort()

for job in jobs:
    name = job["name"]
    skills = job["list"]
    skill.sort()
    if user_skill == skill:
        suggest.append[job]
        
print(suggest)
    
