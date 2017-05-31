#!/usr/bin/env python
from copy import deepcopy

MSG_GCC_ABI_INCOMPETIBILITY = "GCC ABI incompetibility. GridPacks were built with gcc4"
MSG_ARCH_INCOMPETIBILITY = "Architecture incompetibility. GridPacks were built for x86_64"
KNOWN_ERRORS = {"relvals":{}, "addons":{}, "unittests":{}}
KNOWN_ERRORS["relvals"]["CMSSW_9_2_.+"]={
  "slc._amd64_gcc630": {
    "512.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "513.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "515.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "516.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "518.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "519.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "521.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "525.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "526.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "528.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
    "529.0": { "step": 1, "exitcode": 16640, "reason" : MSG_GCC_ABI_INCOMPETIBILITY},
  },
  "slc._aarch64_.+":  {
    "512.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "513.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "514.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "515.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "516.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "517.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "518.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "519.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "520.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "521.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "522.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "523.0": { "step": 1, "exitcode": 31744, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "524.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "525.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "526.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "527.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "528.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "529.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
    "530.0": { "step": 1, "exitcode": 16640, "reason" : MSG_ARCH_INCOMPETIBILITY},
  }
}
KNOWN_ERRORS["relvals"]["CMSSW_9_2_.+"]["slc6_amd64_gcc630"]={"534.0": { "step": 1, "exitcode": 35584, "reason" : MSG_GCC_ABI_INCOMPETIBILITY}}
KNOWN_ERRORS["relvals"]["CMSSW_9_2_.+"]["slc7_amd64_gcc630"]={"534.0": { "step": 1, "exitcode": 62720, "reason" : MSG_GCC_ABI_INCOMPETIBILITY}}

def get_known_errors(release, architecture, test_type):
  if not test_type in KNOWN_ERRORS: return {}
  from re import match
  errs = {}
  for rel in KNOWN_ERRORS[test_type]:
    if not match(rel,release): continue
    for arch in KNOWN_ERRORS[test_type][rel]:
      if not match(arch,architecture): continue
      for test in KNOWN_ERRORS[test_type][rel][arch]:
        errs[test]=KNOWN_ERRORS[test_type][rel][arch][test]
  return errs

if __name__ == "__main__":
  from json import dumps
  print dumps(KNOWN_ERRORS,sort_keys=True,indent=2)
