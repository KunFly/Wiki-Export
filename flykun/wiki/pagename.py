# -*- coding:UTF-8 -*-

class PageName:
    def __init__(self,  pagename,  lang="fr"):
        """
        Give a wiki page name and options, return a list
        """
        self.lang = lang
        self.langset = self.lang_set()
        self.pagename = pagename
        self.list_back = [self.pagename]
        
    def lang_set(self):
        """
        choix language set
        """
        if self.lang == "fr":
            list_prefix = ["Discussion"]
        elif self.lang == "en":
            list_prefix = ["Talk"]
        return list_prefix
    
    def get_page_name(self):
        
        return [self.pagename]
        
    def get_talk_name(self):
        """
        French -> Discussion:pagename
        English -> Talk:pagename
        """
        return ["%s:%s"%(self.langset[0], self.pagename)]
        
    def get_othertalks_name(self):
        """
        Only work for French
        French -> Discussion:pagename/Neutralité
        """
        othertalks = [u"Suppression", u"Neutralité",
                              u"Droit d'auteur", u"Article de qualité", 
                              u"Bon article", u"Lumière sur",
                              u"À faire", u"Traduction"]
        return ["%s:%s/%s"%(self.langset[0], 
                        self.pagename, x) for x in othertalks]
                        
    def get_archive_name(self):
        """
        This is a test fonction
        French -> Discussion:pagename/Archive1
        French -> Discussion:pagename/Archive2
        French -> Discussion:pagename/Archive3
        ...
        """
        range_num = range(10)
        range_num[0] = "" # [0] -> [""]
        return ["%s:%s/Archive%s"%(self.langset[0], 
                        self.pagename, x) for x in range_num]
