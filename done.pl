#!/usr/bin/perl
use strict;
use warnings;


if($#ARGV+1 == 0){
	while(<>)
	{
		chomp( my $line = $_);
		`echo "#$line" >> $0`;
	}
}
elsif($ARGV[0] eq "disp"){
	open (P_FILE, $0);
	my $count = 1;
	while(<P_FILE>)
	{
		if(/^#[^!]/){
			$_ =~ s/^#//;
			print $_;
		}
	}
}
elsif($ARGV[0] eq "del"){
	open (P_FILE, $0);
	my $count = 1;
	my @nums = ();
	while(<P_FILE>)
	{
		if(/^#[^!]/){
			$_ =~ s/^#//;
			print $_ . ": DEL?";
			chomp(my $input = <STDIN>);
			if($input =~ /^[Y|y]/){
				push(@nums, $count);
			}
		}
		$count+=1;
	}
	$count = 0;
	for my $num (@nums){
		my $line = sprintf "sed -i '%dd' %s", ($num-$count), $0;
		system($line);
		$count+=1;
	}
}
#Task 1
#Task 3
