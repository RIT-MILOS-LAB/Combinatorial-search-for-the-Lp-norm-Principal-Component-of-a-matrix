function [ B , P ] = points_forming_cells_D3( X )

    D=size(X,1);
    N=size(X,2);
    [~,~,V]=svd(X,'econ');
    Q=V';
    
    combinations=nchoosek(1:N,2)';
    
    disp('1. Computing cone peaks...')
    for i=1:size(combinations,2)
        Y=Q(:,combinations(:,i)); 
        c=null(Y'); 
        c=c/norm(c);
        peaks(:,i)=mysignwzero(Q'*c);
    end

    disp('2. Naivly resolve ambiguities and gather all binary signatures of the cells (w/ repetitons)...')
    b_pool=[1 1 -1 -1;1 -1 1 -1];
    B_with_repetitions=[];
    for i=1:size(peaks,2)
        for j=1:size(b_pool,2)
            b=peaks(:,i);
            b(b==0)=b_pool(:,j);
            B_with_repetitions=[B_with_repetitions b];
        end
    end
  
    disp('3. Discard redundancies, retain unique binary signatures of cells...')
    Bunq=unique(B_with_repetitions','rows');
    
    
    disp('4. For every binary signature that defines a cell, find the points the nullspaces of which surround it...')
    idx=cell(size(Bunq,1),1);
    for i=1:size(Bunq,1)
        b=Bunq(i,:)';
        for j=1:size(peaks,2)
            peak=peaks(:,j); 
            peak_opposite=-peak;
            if sum(b==peak) >= N-2
                idk=find(b~=peak);
                idx{i}=cat(1,idx{i},idk);
            end
            if sum(b==peak_opposite) >= N-2
                idk=find(b~=peak_opposite);
                idx{i}=cat(1,idx{i},idk);
            end
        end
        signature{i}=b;
    end
    
    
    disp('5. Discard redundancies...')
    cnt=1;
    P=[];
    B=[];
    for i=1:numel(idx)
        idx{i}=unique(idx{i}); 
        card(i)=numel(idx{i});
        
        if card(i)>=3
           if ~isincellarray(idx{i},P)
              P{cnt}=idx{i};
              B{cnt}=signature{i};
              cnt=cnt+1;
           end
        end
    end
   
    expected_number_of_cells=0;
    for i=1:D
        expected_number_of_cells=expected_number_of_cells + nchoosek(N-1,i-1);
    end
    found_number_of_cells=cnt-1;
    fprintf('-------------------------\n')
    fprintf('Expected number of cells: %d\n', expected_number_of_cells)
    fprintf('Number of cells found: %d\n', found_number_of_cells)

end



function [ y ] = mysignwzero( x )

toler=1e-6;
x(abs(x)<toler)=0;
y=sign(x);

end

function [ans]=isincellarray(x,A)
    ans=0;
    for i=1:numel(A)
       a=A{i};
       if numel(a)==numel(x)
           if a==x
               ans=1;
               break;
           end
       end
    end
end
