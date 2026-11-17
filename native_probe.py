import json, platform, sys, traceback
out={'python':sys.version,'platform':platform.platform(),'native_import':False,'simulation_advanced':False}
try:
    import opensim as osim
    out['native_import']=True
    out['opensim_version']=osim.GetVersion()
    model=osim.Model()
    state=model.initSystem()
    out['empty_model_state_size']=state.getNY()
except Exception as exc:
    out['error']=repr(exc)
    out['traceback']=traceback.format_exc()
finally:
    with open('native_probe.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
if not out['native_import']: sys.exit(1)
