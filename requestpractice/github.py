from api.repositories.repos import Repos

class Github():
    def __init__(self,**kwargs):
        self.api_root_url="https://api.github.com"
        self.repos=Repos(self.api_root_url,**kwargs)


if __name__=='__main__':

    # r=Github(token="xxxx")
    # x=r.repos.list_your_repos()
    # print(x.text)

    #调用list_your_repos
    r=Github(username="Soniaxia",password="woainiht258")
    x1=r.repos.list_your_repos()
    print(x1.text)

    data={"direction":"desc"}

    x2=r.repos.list_your_repos(params=data)
    print(x2.text)

    x3=r.repos.list_all_repos()
    print(x3.text)

    x4=r.repos.list_org_repos("TestUpCommunity")
    print(x4.text)

    x = r.repos.list_user_repos("Soniaxia",params=data)
    print(x.text)

    # r=Github(username="Soniaxia",password="woainiht258")
    # x=r.repos.list_your_repos(visibility="private")
    # print(x.text)
    #
    # r=Github(username="Soniaxia",password="woainiht258")
    # x=r.repos.list_your_repos(sort="created",direction="desc")
    # print(x.text)
