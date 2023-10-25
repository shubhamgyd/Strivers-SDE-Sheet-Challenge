def provideJobRecommendation(userKnowledge):
    skills = {
        "marketing strategy": {
            "ans1": 1,
            "ans2": 2,
            "ans3": 3,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 3,
            "ans9": 1,
            "ans10": 1
        },
        "market research": {
            "ans1": 3,
            "ans2": 1,
            "ans3": 2,
            "ans4": 2,
            "ans5": 1,
            "ans6": 4,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "digital marketing": {
            "ans1": 2,
            "ans2": 3,
            "ans3": 3,
            "ans4": 2,
            "ans5": 4,
            "ans6": 2,
            "ans7": 3,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1 
        },
        "financial analysis": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "audit": {
            "ans1": 3,
            "ans2": 1,
            "ans3": 3,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 2,
            "ans8": 1,
            "ans9": 3,
            "ans10": 1
        },
        "accounting software": {
            "ans1": 2,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 3,
            "ans9": 3,
            "ans10": 2
        },
        "financial modeling": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 2,
            "ans4": 1,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "data analysis": {
            "ans1": 4,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1  
        },
        "investment analysis": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 2,
            "ans8": 2,
            "ans9": 2,
            "ans10": 1
        },
        "creativity": {
            "ans1": 2,
            "ans2": 2,
            "ans3": 4,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 1,
            "ans8": 3,
            "ans9": 3,
            "ans10": 2
        },
        "visual design": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 4,
            "ans4": 2,
            "ans5": 3,
            "ans6": 2,
            "ans7": 1,
            "ans8": 2,
            "ans9": 3,
            "ans10": 2
        },
        "adobe creative suite": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 4,
            "ans4": 2,
            "ans5": 2,
            "ans6": 2,
            "ans7": 2,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1
        },
        "recruitment": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 4,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "employee relations": {
            "ans1": 1,
            "ans2": 4,
            "ans3": 3,
            "ans4": 4,
            "ans5": 3,
            "ans6": 2,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "organizational development": {
            "ans1": 5,
            "ans2": 4,
            "ans3": 4,
            "ans4": 5,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 4,
            "ans9": 4,
            "ans10": 2
        },
        "supply chain ans7": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 1,
            "ans4": 3,
            "ans5": 3,
            "ans6": 1,
            "ans7": 4,
            "ans8": 1,
            "ans9": 1,
            "ans10": 2
        },
        "procurement": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 3,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "logistics": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 1,
            "ans4": 2,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 2
        },
        "teaching": {
            "ans1": 3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 3,
            "ans10": 2
        },
        "ans5": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 2,
            "ans5": 4,
            "ans6": 2,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "lesson planning": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 3,
            "ans6": 1,
            "ans7": 3,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1   
        },
        "journalism": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 4,
            "ans5": 4,
            "ans6": 2,
            "ans7": 2,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1
        },
        "interviewing": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 3,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "news ans9": {
            "ans1": 1,
            "ans2": 2,
            "ans3": 3,
            "ans4": 3,
            "ans5": 2,
            "ans6": 2,
            "ans7": 2,
            "ans8": 1,
            "ans9": 4,
            "ans10": 1
        },
        "programming":{
            "ans1":3,
            "ans2": 3,
            "ans3": 2,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "problem-solving":{
            "ans1":3,
            "ans2": 1,
            "ans3": 1,
            "ans4": 3,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "software development":{
            "ans1":3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 2,
            "ans6": 3,
            "ans7": 2,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "data analysis":{
            "ans1": 4,
            "ans2": 2,
            "ans3": 2,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "data visualization":{
            "ans1": 3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 2,
            "ans8": 2,
            "ans9": 2,
            "ans10": 1
        },
        "SQL":{
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        }
    }

    jobs = [
        
        {
            "name":"Marketing Manager",
            "skills":["marketing strategy", "market research", "digital marketing"]
        },
        {
            "name": "Accountant",
            "skills": ["financial analysis", "audit", "accounting software"]
        },
        {
            "name": "Financial Analyst",
            "skills": ["financial modeling", "data analysis", "investment analysis"]
        },
        {
            "name": "Graphic Designer",
            "skills": ["creativity", "visual design", "adobe creative suite"]
        },
        {
            "name": "Human Resources Manager",
            "skills": ["recruitment", "employee relations", "organizational development"]
        },
        {
            "name": "Supply Chain Manager",
            "skills": ["supply chain ans7", "procurement", "logistics"]
        },
        {
            "name": "Teacher",
            "skills": ["teaching", "ans5", "lesson planning"]
        },
        {
            "name": "Journalist",
            "skills": ["journalism", "interviewing", "news ans9"]
        },
        {
            "name": "Software Developer",
            "skills": ["programming", "problem-solving", "software development"]
        },
        {
            "name": "Data Analyst",
            "skills": ["data analysis", "data visualization", "SQL"]
        }
        
    ]

    user_skill = []

    for skill in skills.keys():
        count = 0
        for skill_needs in skills[skill].keys():
            if skills[skill][skill_needs] <= int(userKnowledge[skill_needs]):
                count += 1
        if count == 10:
            user_skill.append(skill)

    suggest = []

    user_skill.sort()
    print(user_skill)
    for job in jobs:
        name = job["name"]
        job_skills = job["skills"]
        job_skills.sort()
        
        count = 0
        for skill in job_skills:
            if skill in user_skill:
                count += 1
        if count == len(job_skills):
            suggest.append(name)
    
    return suggest


if __name__=="__main__":
    a = input("Enter you mathematic skills in scale of 1 to 5: ")
    b = input("Enter your ans2 skill in scale of 1 to 5: ")
    c = input("Enter your ans3 skills in scale of 1 to 5: ")
    d = input("Enter your emotional skills in scale of 1 to 5: ")
    e = input("Enter your ans5s skills in scale of 1 to 5: ")
    f = input("Enter your ans6 skills in scale of 1 to 5: ")
    g = input("Enter your ans7 skills in scale of 1 to 5: ")
    h = input("Enter your ans8 skills in scale of 1 to 5: ")
    i = input("Enter your ans9 skills in scale of 1 to 5: ")
    j = input("Enter your ans10 in scale of 1 to 5: ")
    userKnowledge = {
        "ans1": a,
        "ans2": b,
        "ans3": c,
        "ans4": d,
        "ans5": e,
        "ans6": f,
        "ans7": g,
        "ans8": h,
        "ans9": i,
        "ans10": j
    }
    
    print(provideJobRecommendation(userKnowledge))