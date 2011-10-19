#!/usr/bin/perl

%spec   = ('Chicken Curry'
=>5 );$n=$ARGV[0];$n?one():n();
sub n{		   open FILE,"<",
__FILE__	    or die "UghFU";
while		    (<FILE>){print $_;
}};sub              one{$n = $ARGV[0];
if($n =~ 	   m/menu/){ print
"Specials:\n";foreach $k ( keys
%spec)   { p($spec{$k}
, $k); }		print "\nGeneral ".
"Main Cou"              ."rse M".   "enu:\n";
x();}};			sub p{      my($v,$k
)=@_;print 		""."$k\t\t"."$v";};
		       sub x{ 	    my %m=(
		      'Tando'       .'ori'.
		      ' Chic'       .'ken'.
		     ' Pani'         .'ni'=>        5.50);           foreach
					            $k(keys         %m) {
					               print      "$k\t\t".
					                "$m{$k  }\n"; } }
					                  #And Chips &
					                    #Curry
					                      #€3

