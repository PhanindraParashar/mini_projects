import biogeme.exceptions as excep
raise excep.biogemeError('The file headers.py must not be included anymore. Replace the statement\nfrom headers import *\nby\nfrom biogeme.expressions import Beta, DefineVariable\nglobals().update(database.variables)\n\nReplace also any occurence of bioLogLogit by biogeme.models.loglogit.')
