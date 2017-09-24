#!/bin/bash

###############################################################################
#              Read config files and set variables 
###############################################################################

REMEX_CMD="runaway root file:"

###############################################################################
#                        Script Functions  
###############################################################################

##########  Function: usage  ###############################
usage() {
  echo
  echo "Usage:  $0  <hostlist file>"
  echo
}

###############################################################################
#                  Main Code Body
###############################################################################

if [ -z ${1} ]
then
  HOSTLIST="/var/lib/doaway/hostlist"
else
  HOSTLIST="${1}"
fi

###############################################################################

case ${HOSTLIST} in
  -h|--help)
    usage
    exit 0
  ;;
  *)
${REMEX_CMD}${HOSTLIST} "gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.mandatory  --type bool --set /desktop/gnome/remote_access/enabled true ; gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.mandatory  --type bool --set /desktop/gnome/remote_access/prompt_enabled false ; gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.mandatory  --type bool --set /desktop/gnome/remote_access/view_only false ; init 3 ; sleep 2 ; init 5"
  ;;
esac
