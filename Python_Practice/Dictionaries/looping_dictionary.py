fav_lang ={'bhaskar':'Telugu','Abhiram':'English','Raju':'kannada','Amma':'Hindi'}
per_name =['bhaskar','Amma']

for name in sorted(fav_lang.keys()):
    print(name)

    if name in per_name:
        print('Hi '+name+" Fav language is "+fav_lang[name].upper())