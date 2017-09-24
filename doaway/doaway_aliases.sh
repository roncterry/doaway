#
#    /etc/profile.d/doaway_aliases.sh
#

alias runawayroot='runaway root'
alias runaway.fast='runaway root file:/var/lib/doaway/hostlist'
alias castaway.fast='castaway -l /var/lib/doaway/hostlist'
alias putaway.fast='putaway -l /var/lib/doaway/hostlist'
alias syncaway.fast='syncaway -l /var/lib/doaway/hostlist'
alias walkaway.fast='walkaway -l /var/lib/doaway/hostlist'
alias getaway.fast='getaway -l /var/lib/doaway/hostlist'
alias mkhostlist.fast='mkhostlist -l /var/lib/doaway/hostlist'
alias mkmaclist.fast='mkmaclist /var/lib/dhcp/db/dhcpd.leases > /var/lib/doaway/maclist'
