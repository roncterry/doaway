#!/bin/bash

################################################################################
#              Read config files and set variables 
################################################################################

#  Only set this variable if you want to supply your own 
#   remote execution command and overied the defaults
#REMEX_CMD="runaway root file:"

if [ -z ${REMEX_CMD} ]
then
  if [ -x /usr/bin/runaway ]
  then
    REMEX_CMD="runaway root file:"
  elif [ -x /usr/bin/pssh ]
  then
    REMEX_CMD="pssh -i -h "
  else
    echo
    echo "ERROR:  No parallel remote execution command available"
    echo
    exit 1
  fi
fi

DEF_HOSTLIST="/var/lib/doaway/hostlist"

################################################################################
#                        Script Functions  
################################################################################

##########  Function: usage  ###############################
usage() {
  echo
  echo "Usage:  $0  [on|off]  <hostlist file>"
  echo
}

################################################################################
#                  Main Code Body
################################################################################

if [ -z ${1} ]
then
  echo
  echo "ERROR:  You must specify \"on\" or \"off\""
  usage
  exit 1
elif [ -z ${2} ]
then
  if [ -e "${DEF_HOSTLIST}" ]
  then
  HOSTLIST="${DEF_HOSTLIST}"
  else
    echo
    echo "ERROR:  You must specify a hostlist file"
    usage
    exit 2
  fi
else
  HOSTLIST="${2}"
fi

################################################################################

case ${HOSTLIST} in
  -h|--help)
    usage
    exit 0
  ;;
  *)
   ${REMEX_CMD}${HOSTLIST} ""
  ;;
esac
