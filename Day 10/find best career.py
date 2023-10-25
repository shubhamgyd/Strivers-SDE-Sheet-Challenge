careers = [
    {
        "interests":{
            "mathematics": 1,
            "teamwork": 4,
            "creative_activities": 5,
            "understanding_human_behavior": 3
        },
        "strengths":{
            "rate_strengths": 3,
            "handle_challenges": 4,
            "rate_accomplishment": 4
        },
        "values":{
            "motivation": 4,
            "work_life_balance": 5,
            "work_values": 5,
            "financial_stability": 4
        }
    }
]

user_selection = [
    {
      "name": "Marketing Manager",
      "skills": ["marketing strategy", "market research", "digital marketing"],
      "job_description": "Develop marketing plans, oversee campaigns, analyze consumer trends.",
      "salary_range": "$60,000 - $120,000"
    },
    {
      "name": "Accountant",
      "skills": ["financial analysis", "audit", "accounting software"],
      "job_description": "Prepare financial statements, assess records, ensure tax compliance.",
      "salary_range": "$50,000 - $90,000"
    },
    {
      "name": "Financial Analyst",
      "skills": ["financial modeling", "data analysis", "investment analysis"],
      "job_description": "Analyze financial data, evaluate investment opportunities, provide recommendations.",
      "salary_range": "$55,000 - $100,000"
    },
    {
      "name": "Graphic Designer",
      "skills": ["creativity", "visual design", "Adobe Creative Suite"],
      "job_description": "Create visual concepts, design graphics, produce marketing materials.",
      "salary_range": "$40,000 - $80,000"
    },
    {
      "name": "Human Resources Manager",
      "skills": ["recruitment", "employee relations", "organizational development"],
      "job_description": "Oversee HR functions, manage employee relations, and develop the workforce.",
      "salary_range": "$60,000 - $120,000"
    },
    {
      "name": "Supply Chain Manager",
      "skills": ["supply chain management", "procurement", "logistics"],
      "job_description": "Manage end-to-end supply chain operations, optimize processes.",
      "salary_range": "$70,000 - $130,000"
    },
    {
      "name": "Teacher",
      "skills": ["teaching", "communication", "lesson planning"],
      "job_description": "Educate students, create lesson plans, assess student progress.",
      "salary_range": "$40,000 - $80,000"
    },
    {
      "name": "Journalist",
      "skills": ["journalism", "interviewing", "news writing"],
      "job_description": "Research and report news, conduct interviews, write articles.",
      "salary_range": "$40,000 - $80,000"
    },
    {
      "name": "Software Developer",
      "skills": ["programming", "problem-solving", "software development"],
      "job_description": "Develop and maintain software applications.",
      "salary_range": "$70,000 - $130,000"
    },
    {
      "name": "Data Analyst",
      "skills": ["data analysis", "data visualization", "SQL"],
      "job_description": "Analyze data, create reports, and provide insights.",
      "salary_range": "$55,000 - $100,000"
    },
    {
      "name": "Architect",
      "skills": ["architectural design", "CAD software", "project management"],
      "job_description": "Design buildings, create plans, oversee construction projects.",
      "salary_range": "$60,000 - $120,000"
    },
    {
      "name": "Biomedical Scientist",
      "skills": ["biomedical research", "laboratory techniques", "data analysis"],
      "job_description": "Conduct research in biomedical sciences, analyze data, publish findings.",
      "salary_range": "$60,000 - $110,000"
    },
    {
      "name": "Environmental Scientist",
      "skills": ["environmental research", "data collection", "sustainability"],
      "job_description": "Study environmental issues, collect and analyze data, advise on sustainability.",
      "salary_range": "$50,000 - $90,000"
    },
    {
      "name": "Psychologist",
      "skills": ["psychology", "counseling", "research"],
      "job_description": "Assess and treat mental health issues, conduct research in psychology.",
      "salary_range": "$60,000 - $120,000"
    },
    {
      "name": "Dietitian/Nutritionist",
      "skills": ["nutrition counseling", "diet planning", "health education"],
      "job_description": "Provide nutrition guidance, develop dietary plans, promote healthy eating.",
      "salary_range": "$50,000 - $80,000"
    }
]

for selection in user_selection:
    l = selection["skills"]
    for i in range(len(l)):
        print(l[i])

# d = dict()
# for selection in user_selection:
#     name = selection["name"]
#     l = selection["skills"]
#     count = 0
#     for i in range(len(l)):
#         count += 1
#     d[name] = count
d = set()
for selection in user_selection:
    name = selection["name"]
    d.add(name)
    
    
print(d)