# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:38:01 2024

@author: pspealman

python tiny_rgi_combiner.py -i mapfile.tab
"""
import argparse 
import pandas as pd


parser = argparse.ArgumentParser(add_help=True)

''' IO '''
parser.add_argument('-i',"--input_mapfile", help="Path to map file Two column, tab delimited, first column: sample name, second column: file path")
parser.add_argument('-o',"--output_path", help="Path for output", default = '.')
parser.add_argument('-test',"--test", help="Run Test", action='store_true')

args = parser.parse_args()
''''''

def parse_rgi_aro(sample_name, sample_dict, hits_dict, col_name):
    sample_col_name = ('sample_{sample_name}').format(
        sample_name = sample_name)
    
    for uid in sample_dict:
        selected_val = sample_dict[uid][col_name]
        
        if selected_val not in hits_dict:
            hits_dict[selected_val] = {}
            
        if sample_col_name not in hits_dict[selected_val]:
            hits_dict[selected_val][sample_col_name] = 0
            
        hits_dict[selected_val][sample_col_name] += 1
        
    return(hits_dict)   

def output_results(hits_dict, col_name):
    
    type_name = col_name.replace(' ', '_')
    
    outfile_name = ('{out_path}/RGI_{type_name}.csv').format(
        out_path = args.output_path,
        type_name = type_name)
    
    hits_df = pd.DataFrame.from_dict(hits_dict, orient='index')
    hits_df = hits_df.fillna(0) 
    hits_df.to_csv(outfile_name)
    
mapfile = open(args.input_mapfile)

aro_hits = {} # Best_Hit_ARO
arm_hits = {} # AMR Gene Family
res_hits = {} # Resistance Mechanism
drg_hits = {} # Drug Class

for line in mapfile:
    if line[0] != '#':
        line = line.strip()
        sample_name, sample_path = line.split('\t')
        
        outline = ('Processing sample: {}').format(sample_name)
        
        print(outline)
        
        try:
            sample_df = pd.read_table(sample_path, index_col=0)
            sample_dict = sample_df.to_dict('index')
            #aro_hits = {} # Best_Hit_ARO
            aro_hits = parse_rgi_aro(sample_name, sample_dict, aro_hits, 'Best_Hit_ARO')
            
            #arm_hits = {} # AMR Gene Family
            arm_hits = parse_rgi_aro(sample_name, sample_dict, arm_hits, 'AMR Gene Family')
            
            #res_hits = {} # Resistance Mechanism
            res_hits = parse_rgi_aro(sample_name, sample_dict, res_hits, 'Resistance Mechanism')
            
            #drg_hits = {} # Drug Class
            drg_hits = parse_rgi_aro(sample_name, sample_dict, drg_hits, 'Drug Class')
            
        except:
            outline = ('Unable to open {sample_path}\n').format(sample_path = sample_path)
            print(outline)
            
#aro_hits = {} # Best_Hit_ARO
output_results(aro_hits, 'Best_Hit_ARO')

#arm_hits = {} # AMR Gene Family
output_results(arm_hits, 'AMR Gene Family')

#res_hits = {} # Resistance Mechanism
output_results(res_hits, 'Resistance Mechanism')

#drg_hits = {} # Drug Class
output_results(drg_hits, 'Drug Class')



            
            