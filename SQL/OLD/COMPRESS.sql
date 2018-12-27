drop table xx_comp;

create table xx_comp (
seq_no number,
col1 varchar2(2),
col2 varchar2(2),
col3 varchar2(2));

insert into xx_comp values(1,'','','T1');
insert into xx_comp values(2,'','','Q1');
insert into xx_comp values(3,'','P1','');
insert into xx_comp values(4,'P2','','');
insert into xx_comp values(5,'','Q2','');
insert into xx_comp values(6,'T2','','');
insert into xx_comp values(7,'','','P3');
insert into xx_comp values(8,'P4','','');


select * from xx_comp;



begin
  FOR r_col1 in (select rownum, col1, rowid from xx_Comp where col1 is not null)
  LOOP
    
    UPDATE xx_comp
    set    col1=null
    where  rowid=r_col1.rowid;
    
    update xx_comp
    set    col1=r_col1.col1
    WHERE  seq_no=r_col1.rownum;
    
  END LOOP;
  --
  FOR r_col2 in (select rownum, col2, rowid from xx_Comp where col2 is not null)
  LOOP
    UPDATE xx_comp
    set    col2=null
    where  rowid=r_col2.rowid;

    update xx_comp
    set    col2=r_col2.col2
    WHERE  seq_no=r_col2.rownum;
    

  END LOOP;  
  --
  
  FOR r_col3 in (select rownum, col3, rowid from xx_Comp where col3 is not null)
  LOOP
    UPDATE xx_comp
    set    col3=null
    where  rowid=r_col3.rowid;
    
    update xx_comp
    set    col3=r_col3.col3
    WHERE  seq_no=r_col3.rownum;
    
    
  END LOOP;  
  --
  
  DELETE xx_comp where col1 is null and col2 is null and col3 is null;
end;
/


select  * from xx_comp;