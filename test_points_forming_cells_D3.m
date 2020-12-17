clear all
close all
clc
%%
D=3;
N=10;

X=randn(D,N);
[ B , P ] = points_forming_cells_D3( X );