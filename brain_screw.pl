#!/usr/bin/perl
use strict;
use warnings;

print qq(

#include<stdio.h>
#include<stdlib.h>
int main(int argc, char * argv[]){
	unsigned char * ptr = malloc(sizeof(unsigned char *) * 30000);
);

my %comps = (
	">" => "++ptr;",
	"<" => "--ptr;",
	"+" => "++*ptr;",
	"-" => "--*ptr;",
	"." => "putchar(*ptr);",
	"," => "*ptr = getchar();",
	"[" => "while(*ptr) {",
	"]" => "}"
);
my $output = "";
while(<>){
	my @chars = split //, $_;
	foreach my $char (@chars){
		foreach my $key (keys %comps){
			if($char eq $key){
				$output .= $comps{$key};
			}
		}
	}
}
print $output;
print "\nreturn 0;\n}";
