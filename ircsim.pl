#!/usr/bin/perl
use strict;
use warnings;

my $time = 0;

while(<>) {
	my $line = $_;
	#print $line . "\n";
	unless (m/^\*\*\*\*/ || m/^\s*$/){
		my @parts = split;
		my ($hours, $mins, $secs) = split(":", $parts[2]);
		#printf "Count of parts is %d %s %d %d %d\n", $#parts, $parts[2], $hours, $mins, $secs;
		my @sentence = splice ( @parts, 3, $#parts);
		print join(" ", @sentence) . "\n";
		my $temp_time = $hours * 60*60;
		$temp_time += $mins * 60;
		$temp_time += $secs;
		if($time == 0){$time = $temp_time}
		#printf "sleeping for %d %d %d %d %d %d\n",$hours, $mins, $secs, $time, $temp_time,$time - $temp_time;
		sleep($temp_time - $time);
		$time = $temp_time;
	}
}
