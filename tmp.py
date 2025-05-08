import json
import os

def load_jsonl(data_path):
    with open(data_path,'r') as f:
        json_strs = f.readlines()
    json_objs = [json.loads(jstr)['code'] for jstr in json_strs]
    for item in json_objs:
        if item.startswith("@Override\n    public ItemStream removeFirstMatching(Filter filter, Transaction transaction) throws MessageStoreException\n    {\n        if (TraceComponent.isAnyTracingEnabled() && tc.isEntryEnabled())\n            SibTr.entry(this, tc, \"removeFirstMatching\", new Object[] { filter, transaction });\n\n        if ("):
            print(item)
            return


data_path = "/mnt/disk2/liwei/01-code/CodeMark-FSE/data/java/final/jsonl/train"
for file in os.listdir(data_path):
    if file.endswith('jsonl'):
        load_jsonl(os.path.join(data_path, file))