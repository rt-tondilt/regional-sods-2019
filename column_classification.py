t = 't' # truth value
i = 'i' # integer
c = 'c' # categorical
o = 'o' # can enter other answer

m = 'm' #
m3 = 'm3'
n = 'n'
date = 'date'


columns = [

# Basic Information
['Respondent',i],
['MainBranch',c],
['Hobbyist',t],
['OpenSourcer',c],
['OpenSource',c],
['Employment',c],
['Country',c],

# Education, work, and career
['Student',c],
['EdLevel',c,o],
['UndergradMajor',c,o],
['EduOther',m],
['OrgSize',c],
['DevType',m,o],
['YearsCode',i],
['Age1stCode',i],
['YearsCodePro',i],
['CareerSat',c],
['JobSat',c],
['MgrIdiot',c],
['MgrMoney',c],
['MgrWant',c],
['JobSeek',c],
['LastHireDate',c],
['LastInt',m],
['FizzBuzz',t],
['JobFactors',m3],
['ResumeUpdate',c],
['CurrencySymbol',c],
['CurrencyDesc',c],
['CompTotal',i],
['CompFreq',c],
['ConvertedComp',n],
['WorkWeekHrs',n],
['WorkPlan',c,o],
['WorkChallenge',m3],
['WorkRemote',c],
['WorkLoc',c],
['ImpSyn',c],
['CodeRev',c],
['CodeRevHrs',n],
['UnitTests',c],
['PurchaseHow',c,o],
['PurchaseWhat',c],

# Tech and tech culture
['LanguageWorkedWith',m,o],
['LanguageDesireNextYear',m,o],
['DatabaseWorkedWith',m,o],
['DatabaseDesireNextYear',m,o],
['PlatformWorkedWith',m,o],
['PlatformDesireNextYear',m,o],
['WebFrameWorkedWith',m,o],
['WebFrameDesireNextYear',m,o],
['MiscTechWorkedWith',m,o],
['MiscTechDesireNextYear',m,o],
['DevEnviron',m,o],
['OpSys',c,o],
['Containers',m],
['BlockchainOrg',c],
['BlockchainIs',c],
['BetterLife',t],
['ITperson',c],
['OffOn',c],
['SocialMedia',c,o],
['Extraversion',c],
['ScreenName',c],

# Stack Overflow usage and community
['SOVisit1st',date],
['SOVisitFreq',c],
['SOVisitTo',m],
['SOFindAnswer',c],
['SOTimeSaved',c],
['SOHowMuchTime',c],
['SOAccount',c],
['SOPartFreq',c],
['SOJobs',c],
['EntTeams',c],
['SOComm',c],
['WelcomeChange',c],
['SONewContent',m],

# Demographics
['Age',i],
['Gender',m,o],
['Trans',c,o],
['Sexuality',m,o],
['Ethnicity',m,o],
['Dependents',c],

# Final thoughts / survey review
['SurveyLength',c],
['SurveyEase',c],

]
