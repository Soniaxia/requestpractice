from core.rest_client import RestClient

class Repos(RestClient):
    def __init__(self,api_root_url,**kwargs):
        super(Repos,self).__init__(api_root_url,**kwargs)

    # def list_your_repos(self,visibility=None,affiliation=None,type=None,sort=None,direction=None):
    #     params={"visibility":visibility,
    #             "affiliation":affiliation,
    #             "type":type,
    #             "sort":sort,
    #             "direction":direction}
    #     return self.get("/user/repos",params=params)

    def list_your_repos(self, **kwargs):
        '''

        http://developer.github.com/v3/repos/#list-your-repositories
        :param kwargs:

        '''
        return self.get("/user/repos", **kwargs)

    def list_user_repos(self,username,**kwargs):
        '''
        https://developer.github.com/v3/repos/#list-user-repositories
        :param username:username
        :param kwargs:
        :return:
        '''
        return self.get("/user/{}/repos".format(username),**kwargs)


    def list_org_repos(self,org,**kwargs):
        '''
        https://developer.github.com/v3/repos/#list-organization-repositories
        :param org:
        :param kwargs:
        :return:
        '''
        return self.get("/orgs/{}/repos".format(org),**kwargs)

    def list_all_repos(self,**kwargs):
        '''
        https://developer.github.com/v3/repos/#list-all-public-repositories
        :param kwargs:
        :return:
        '''
        return self.get("/repositories",**kwargs)

    def create_user_repo(self,**kwargs):
        return self.post("/user/repos",**kwargs)

    def create_organization_repo(self,org,**kwargs):
        return self.post("/org/{}/repos".format(org),**kwargs)

    def get_repo(self,owner,repo,**kwargs):
        '''

        :param owner:
        :param repo:
        :param kwargs:
        :return:
        '''
        return self.get("/repos/{}/{}".format(owner,repo),kwargs)

    def edit_repo(self,owner,repo,**kwargs):
        '''

        :param owner:
        :param repo:
        :param kwargs:
        :return:
        '''
        return self.patch("/repos/{}/{}".format(owner,repo),**kwargs)
