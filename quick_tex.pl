#!/usr/bin/perl
use strict;
use warnings;

my %headvars = (
	"t:" => "\\title{",
	"a:" => "\\author{",
	"d:" => "\\date{",
);

my %vars = (
	"sect:" => "\\section\*{%s}",
	"subsect:" => "\\subsection\*{%s}",
	"li:" => "\\begin{enumerate}",
	"eli:" => "\\end{enumerate}",
	"-" => "\\item %s"
);

my @head_liners = ();
my @lines = ();

while(<>)
{
	my $temp_line= $_;
	my $head_found = 0;
	for my $head_key (keys %headvars)
	{
		if($temp_line =~ m/^$head_key/)
		{
			$head_found = 1;
			$temp_line =~ s/$head_key/$headvars{$head_key}/;
			chomp($temp_line);
			$temp_line .= "}";
			last;
		}
	}
	if($head_found)
	{
		push(@head_liners, $temp_line);
		next;
	}
	for my $key (keys %vars)
	{
		if($temp_line =~ m/^$key/)
		{
			$temp_line =~ s/$key//;
			my $template = $vars{$key};
			chomp($temp_line);
			$template =~ s/%s/$temp_line/g;
			$temp_line = $template;
			last;
		}
	}
	push(@lines, $temp_line);
}

print "\\documentclass{article}\n";
my $title = 0;
for my $line (@head_liners)
{
	if($line =~ m/title/)
	{
		$title =1;
	}
	print $line . "\n";
}
unless($title == 1){
	my $date = `date +'%d-%m-%y'`;
	chomp($date);
	printf "\\title{Notes %s}\n", $date;
}
print "\\begin{document}\n \\maketitle \n";

for my $line (@lines){

if (not $line =~ m/^\\/)
{
$line =~ s/_/\\textunderscore /g;
$line =~ s/{/\\{/g;
$line =~ s/}/\\}/g;
}
$line =~ s/</ \\langle /g;
$line =~ s/>/ \\rangle /g;
print $line. "\n";
}

print "\\end{document}";

