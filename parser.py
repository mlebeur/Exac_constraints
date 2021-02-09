import os, pandas, csv, re
import numpy as np
from biothings.utils.dataload import dict_convert, dict_sweep
from biothings import config
logging = config.logger
def load_Exac_constraints(data_folder):
    infile = os.path.abspath("/opt/biothings/GRCh37/ExAC_constraints/r0.3.1/ExacConstraints.tsv")
    assert os.path.exists(infile)
    dat = pandas.read_csv(infile,sep="\t",squeeze=True,quoting=csv.QUOTE_NONE).to_dict(orient='records')
    results = {}
    for rec in dat:
        _id = rec["symbol"]
        process_key = lambda k: k.replace(" ","_").lower()\nrec = dict_convert(rec,keyfn=process_key)\nresults.setdefault(_id,[]).append(rec)
    for _id,docs in results.items():
        doc = {"_id": _id, "Exac_constraints" : docs}
        yield doc
