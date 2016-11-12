%1 %1.A small matrix A having a 0 on the diagonal;
rng(1)
n = 5;
mmax = 100;
mat1 = 2*mmax*rand(n)-mmax;
mat = mat1+diag(sum(abs(mat1),2).*sign(diag(mat1)));
mat(3,3)=0;
mat=abs(mat);

%2.A small diagonally dominant matrix A;
rng(1)
n = 5;
mmax = 100;
mat1 = 2*mmax*rand(n)-mmax;
mat = abs(mat1+diag(sum(abs(mat1),2).*sign(diag(mat1))));
mat=abs(mat)

%3.A small matrix A such that A 
%    has no 0 on the main diagonal
%    A is not diagonally dominant
%    all of the eigenvalues of C have absolute value < 1.
%    What do you expect to happen in this case?
A=[ 2 0.5 1.5 ; 2 5 6; 1 0.7 4];
D=[2 0 0; 0 5 0; 0 0 4];
C = -inv(D)*(A-D)
e = abs(eig(C))

%4.  A small matrix A such that
%    A has no 0 on the main diagonal
%    A is not diagonally dominant
%    one or more of the eigenvalues of C have absolute value > 1.
%    What do you expect to happen in this case?
A=[ 2 0.5 8.5 ; 2 5 6; 1 0.7 4];
D=[2 0 0; 0 5 0; 0 0 4];
C = -inv(D)*(A-D)
e = abs(eig(C))

%5. A small matrix A such that
%    A has no 0 on the main diagonal
%    A is not diagonally dominant
%    Ct*C and all eigenavlues abs < 1
A=[ 2 0.5 0.2 ; 0.4 0.7 0.4; 0.1 0.7 2]
D=[2 0 0; 0 1 0; 0 0 2];
C = -inv(D)*(A-D);
newC=transpose(C)*C;
e = abs(eig(newC))
