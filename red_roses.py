import requests                                                           #import for api response
import json                                                               #import for json support
def call_api_for_repo_name(query,page):
    #api.git does not give respone in a sorted order of forks hence we have to get all the responses and sort out self
    #this function will return all the json data till the last page
    repo_data = []
    req = requests.get(query+str(page));
    if(str(req)=='<Response [200]>'):
        repo_data = req.json()
        if(len(repo_data)>99):
            repo_data.extend(call_api_for_repo_name(query,page+1))
        return repo_data
    else:
        print(req)

org_name,n,m = list(input('input name n m\n').split())

query_for_repo = "https://api.github.com/orgs/"+org_name+"/repos?type=fork&per_page=100&page="     #string for calling api for repos;
repo_data = call_api_for_repo_name(query_for_repo,1);                                              #function call
try:
    repo_data = sorted(repo_data,key= lambda i:i["forks"],reverse=True)                            #sorting according to the forks
except:
    print("empty data")
for i in repo_data:
   print(i['name'])
try:
    for i in range(int(n)):
        repo_name = repo_data[i]['name']
        print(repo_name);
        query_for_collab = "https://api.github.com/repos/"+org_name+"/"+repo_name+"/contributors"      #string for calling api for collabiraters
        req = requests.get(query_for_collab);                                                          # api call
        print()
        print("collab:")
        if(str(req) == '<Response [200]>'):
            pass
        else:
            print(req)
        collab_data = req.json();
        try:
            for j in range(int(m)):
                print(collab_data[j]['login'],collab_data[j]['contributions'])
        except Exception as e:
            pass
        print()
except Exception as e:
    pass
    
#speed of the program depends upon the speed and response of the api
#api calls  from user to collabration organizations are restricted for every 24 hours
#for unlimited calls we have to send out clint id and clint seceret
#for more info refer https://docs.github.com/en/free-pro-team@latest/rest/reference/rate-limit
        
    
        
    
