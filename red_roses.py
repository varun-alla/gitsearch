import requests                                                           #import for api response
import json                                                               #import for json support
import math
def call_api(query,n):
    #function retrives data using api.github can be re used for other purposes also
    re_data = []
    k=int(math.ceil(n/100))                    #allows us to move to next page to get enough data
    for page in range(1,k+1):
        req = requests.get(query+str(page));
        #print(query+str(page))
        if(str(req) == '<Response [200]>'):
            pass
        else:
            print(req)
            return []
        data = req.json()
        if(isinstance(data, dict) ):                          
            re_data.extend(data['items'])
        elif(isinstance(data,list) ):
            re_data.extend(data)
    return re_data;
    
def main(org_name,n,m):

    access_token="access_token="+"copy access token here"        #access token use to get 5000 req per hour #copy your access token to this 

    access_token_cond=access_token+"&token_type=bearer"

    access_token_cond=""                                          #add access token and comment this line for more req per houe

    query_for_repo = "https://api.github.com/search/repositories?q=org:"+org_name+"&sort=forks&order=desc&per_page=100&"+access_token_cond+"&page="     #string for calling api for repos;

    repo_data = call_api(query_for_repo,int(n));                                              #function call

    try:
        for i in range(int(n)):
            repo_name = repo_data[i]['name']
            forks = repo_data[i]['forks']
            print(repo_name,forks);
            query_for_collab = "https://api.github.com/repos/"+org_name+"/"+repo_name+"/contributors?per_page=100&"+access_token_cond     #string for calling api for collabiraters                                                         # api call
            print()
            print("contributors:")
            collab_data = call_api(query_for_collab,int(m))
            try:
                for j in range(int(m)):
                    print(collab_data[j]['login'],collab_data[j]['contributions'])
            except Exception as e:
                pass
            print()
    except Exception as e:
        print()

if __name__=='__main__':
    try:
        org_name,n,m = list(input('input name n m\n').split())
        int(n)
        int(m)
        main(org_name,n,m)
    except:
        print("enter proper inputs")
    

#speed of the program depends upon the speed and response of the api
#api calls  from user to collabration organizations are restricted for every 24 hours
#for unlimited calls we have to send out clint id and clint seceret
#for more info refer https://docs.github.com/en/free-pro-team@latest/rest/reference/rate-limit
        
    
        
    
