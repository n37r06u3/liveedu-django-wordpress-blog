from .models import *

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model in [WpCommentmeta,WpComments,WpLinks,WpOptions,WpPostmeta,WpPosts,WpTermmeta,WpTermRelationships,WpTerms,WpTermTaxonomy,WpUsermeta,WpUsers]:
            return 'wordpress'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model in [WpCommentmeta,WpComments,WpLinks,WpOptions,WpPostmeta,WpPosts,WpTermmeta,WpTermRelationships,WpTerms,WpTermTaxonomy,WpUsermeta,WpUsers]:
            return 'wordpress'
        return None