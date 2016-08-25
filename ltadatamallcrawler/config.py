import os, re, yaml


#define the regex pattern that the parser will use to 'implicitely' tag your node
pattern = re.compile( r'^\<%= ENV\[\'(.*)\'\] %\>(.*)$' )

#now define a custom tag ( say pathex ) and associate the regex pattern we defined
yaml.add_implicit_resolver ( "!pathex", pattern )

#at this point the parser will associate '!pathex' tag whenever the node matches the pattern

#you need to now define a constructor that the parser will invoke
#you can do whatever you want with the node value
def pathex_constructor(loader,node):
  value = loader.construct_scalar(node)
  envVar, remainingPath = pattern.match(value).groups()
  return os.environ[envVar] + remainingPath

#'register' the constructor so that the parser will invoke 'pathex_constructor' for each node '!pathex'
yaml.add_constructor('!pathex', pathex_constructor)



with open('settings.yaml', 'r') as stream:
    try:
        settings = yaml.load(stream)
    except yaml.YAMLError as e:
        print(e)
        settings = {}
