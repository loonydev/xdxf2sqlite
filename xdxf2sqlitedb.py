#! /usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, ArgumentTypeError, RawDescriptionHelpFormatter
import sqlite3
from xml.etree import ElementTree

EXTRA_HELP = """

  _      ____   ____  _   ___     __     _____              
 | |    / __ \ / __ \| \ | \ \   / /    |_   _|             
 | |   | |  | | |  | |  \| |\ \_/ /       | |  _ __   ___   
 | |   | |  | | |  | | . ` | \   /        | | | '_ \ / __|  
 | |___| |__| | |__| | |\  |  | |        _| |_| | | | (__ _ 
 |______\____/ \____/|_| \_|  |_|       |_____|_| |_|\___(_)
                                                            
                                                            	
                                                             	

Example usage:
python xdxf2sqlitedb.py -i dict.xdxf -o test.db -d dictionary -k KEY -a ANS
"""

def create_db_file(output,table,key,answer):
	con = sqlite3.connect(output)
	cur = con.cursor()
	cur.execute('CREATE TABLE '+table+' (id INTEGER PRIMARY KEY, '+ key+' TEXT, '+answer+' TEXT)')
	con.commit()
	return con,cur

def read_xdxf(input_file):
	data=[]
	with open(input_file) as input_file:
		tree = ElementTree.parse(input_file)
	return [[record.text,record.tail] for record in tree.iter('k')]
		
def write_xdxf_to_db(data_xdxf,connection,cursor,table,key,answer):
	sql_query='INSERT INTO '+ table +' (id, ' +key+',' +answer+') VALUES(?,?,?)'
	for item in data_xdxf:
		cursor.execute(sql_query,[None,item[0],item[1]])
	connection.commit()
	connection.close()

def main(args):
	connection,cursor=create_db_file(output=args.db_output,table=args.db_table,key=args.db_key,answer=args.db_answer)
	write_xdxf_to_db(data_xdxf=read_xdxf(input_file=args.xdxf_input),connection=connection,cursor=cursor,table=args.db_table,key=args.db_key,answer=args.db_answer)


if __name__ == '__main__':
	parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description='Script for converting XDXF to DB', add_help=True, usage=EXTRA_HELP)
	
	parser.add_argument("-i", "--input-file", dest="xdxf_input", type=str, default='',
		help="File for conversion in format XDXF")

	parser.add_argument("-o", "--output", dest="db_output", type=str,
		help="Output file with\\for SQLite database.")

	parser.add_argument("-d", "--table", dest="db_table", type=str,default='dictionary',
		help="Change the name of the table. [Default=%(default)s]")

	parser.add_argument("-k", "--key", dest="db_key", type=str,default='KEY',
		help="Change the name of the key column. [Default=%(default)s]")

	parser.add_argument("-a", "--answer", dest="db_answer", type=str,default='ANS',
		help="Change the name of the answer column. [Default=%(default)s]")


	
	args = parser.parse_args()
	main(args)