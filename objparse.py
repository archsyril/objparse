from configparser import ConfigParser

def understand_with(cfg, cls, section_name=None):
  if type(cfg) is str:
    fn = cfg
    cfg = ConfigParser(); cfg.read(fn)
  objs = []
  if "CLASS" in cfg:
    del cfg["CLASS"]
  for section in cfg.keys():
    if section == "DEFAULT": continue
    if section_name:
      cfg[section].update({section_name: section})
    objs.append(cls(**cfg[section]))
  return objs

def understand(fn, *methods):
  cfg = ConfigParser(); cfg.read(fn)
  cls, objs, ci = None, [], cfg["CLASS"]
  clsname, secname = ci.pop("__name__"), ci.pop("__section__")
  dk = list(ci.keys())
  methods = {m.__name__:m for m in methods}
  if "__init__" not in methods:
    ns = {}
    exec("def __init__(i,*,%s):%s" % (",".join(dk),
      "".join(("\n i.{}="+(ci[d] if ci[d].lower() != "none" else "{}")).format(d, d)for d in dk)), ns)
    methods.update(ns)
  cls = type(clsname, (object,), methods)
  del dk, methods
  return (cls, understand_with(cfg, cls, secname))
