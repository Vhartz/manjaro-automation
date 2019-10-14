#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from tqdm import tqdm
import os, subprocess, time

__title__ = 'pyjaro'
__version__ = '0.1'
__author__ = 'Vitor Amorim'
__license__ = 'MIT 2019'
__copyright__ = 'Copyright 2019 Vitor Amorim'

def progress_connecting():
	with tqdm(total=20, desc='Connecting..') as pbar:
		for i in range(20):
			time.sleep(0.1)
			pbar.update(1)

def progress_20():
	with tqdm(total=20, desc='Loading Modules..') as pbar:
		for i in range(20):
			time.sleep(0.1)
			pbar.update(1)

date = time.ctime()
parser = ArgumentParser(prog='PyJaro',
						usage='Passe os Argumentos\n Ex: pyjaro.py -h \n Ex: pyjaro.py -r -l',
						description='Script de Automação para Manjaro Linux',
						epilog='Vitor Amorim <vhartzamorimg2@gmail.com> github.com/Vhartz\n',
						fromfile_prefix_chars='@')

#adcionar argumento de linha de comando
parser.add_argument('-v','--verbose', action='store_true',help='description command')
parser.add_argument('-r','--repo', action='store_true',help='Scan for Brazilian repository')
parser.add_argument('-l','--log', action='store_true',help='Create output log for scan')
parser.add_argument('-t','--time', action='store_true',help='Set localtime')
args = parser.parse_args()
# cada if chama a sequencia de comando ao usar o argumento colocar and para adiconar mais de um argumento no comando
if args.verbose:
    print("ok")

if args.repo:
	progress_connecting()
	os.system('pacman-mirrors --country Brazil')

if args.time:
	progress_20()
	print(date)

if args.log:
	progress_20()
	log_mirror = subprocess.getoutput('cat /etc/pacman.d/mirrorlist')
	save_log = open('log_scan.txt','a')
	save_log.write('\t Scan Finished in \t' + date + '\n ')
	save_log.close()
