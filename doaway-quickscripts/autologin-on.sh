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
    REMEX_CMD="pssh -i -l root -h "
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
  echo "Usage:  $0  <username>  <hostlist file>"
  echo
}

################################################################################
#                  Main Code Body
################################################################################

if [ -z ${1} ]
then
  echo
  echo "ERROR:  You must specify a username to autologin"
  usage
  exit 2
elif [ -z ${2} ]
then
  if [ -e "${DEF_HOSTLIST}" ]
  then
  HOSTLIST="${DEF_HOSTLIST}"
  else
    echo
    echo "ERROR:  You must specify a hostlist file"
    usage
    exit 3
  fi
else
  USERNAME=${1}
  HOSTLIST="${2}"
fi

################################################################################

case ${USERNAME} in
  -h|--help)
    usage
    exit 0
  ;;
  *)
    ${REMEX_CMD}${HOSTLIST} "sed -i 's/^DISPLAYMANAGER_AUTOLOGIN=\"\"/DISPLAYMANAGER_AUTOLOGIN=\"${USERNAME}\"/g' /etc/sysconfig/displaymanager;init 3;sleep 5;init 5"
  ;;
esac
