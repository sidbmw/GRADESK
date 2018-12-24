drop table EOM_MAIN_SCREEN_LAYOUT;

select * from EOM_MAIN_SCREEN_LAYOUT;



begin
  FOR r_x_inc in (select rownum, x_inc, rowid from EOM_MAIN_SCREEN_LAYOUT where x_inc is not null)
  LOOP
    
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_inc=null
    where  rowid=r_x_inc.rowid;
    
    update EOM_MAIN_SCREEN_LAYOUT
    set    x_inc=r_x_inc.x_inc
    WHERE  seq_no=r_x_inc.rownum;
    
  END LOOP;
  --
  FOR r_x_r in (select rownum, x_r, rowid from EOM_MAIN_SCREEN_LAYOUT where x_r is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_r=null
    where  rowid=r_x_r.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_r=r_x_r.x_r
    WHERE  seq_no=r_x_r.rownum;
    

  END LOOP;  
  --
  
  FOR r_x_1mm in (select rownum, x_1mm, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1mm is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1mm=null
    where  rowid=r_x_1mm.rowid;
    
    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1mm=r_x_1mm.x_1mm
    WHERE  seq_no=r_x_1mm.rownum;
    
    
  END LOOP;  
  --
  
  FOR r_x_1ms1 in (select rownum, x_1ms1, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1ms1 is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1ms1=null
    where  rowid=r_x_1ms1.rowid;
    
    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1ms1=r_x_1ms1.x_1ms1
    WHERE  seq_no=r_x_1ms1.rownum;
    
    
  END LOOP;
  --
  
  FOR r_x_1ms1 in (select rownum, x_1ms1, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1ms1 is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1ms1=null
    where  rowid=r_x_1ms1.rowid;
    
    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1ms1=r_x_1ms1.x_1ms1
    WHERE  seq_no=r_x_1ms1.rownum;
    
    
  END LOOP;
  --
  
  FOR r_x_1 in (select rownum, x_1, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1 is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1=null
    where  rowid=r_x_1.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1=r_x_1.x_1
    WHERE  seq_no=r_x_1.rownum;


  END LOOP;
  --
  
  FOR r_x_1s1p in (select rownum, x_1s1p, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1s1p is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1s1p=null
    where  rowid=r_x_1s1p.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1s1p=r_x_1s1p.x_1s1p
    WHERE  seq_no=r_x_1s1p.rownum;


  END LOOP;
  --
  FOR r_x_1p in (select rownum, x_1p, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1p is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1p=null
    where  rowid=r_x_1p.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1p=r_x_1p.x_1p
    WHERE  seq_no=r_x_1p.rownum;


  END LOOP;
  --
  FOR r_x_1ps2m in (select rownum, x_1ps2m, rowid from EOM_MAIN_SCREEN_LAYOUT where x_1ps2m is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_1ps2m=null
    where  rowid=r_x_1ps2m.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_1ps2m=r_x_1ps2m.x_1ps2m
    WHERE  seq_no=r_x_1ps2m.rownum;


  END LOOP;
  --
  
  FOR r_x_2m in (select rownum, x_2m, rowid from EOM_MAIN_SCREEN_LAYOUT where x_2m is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_2m=null
    where  rowid=r_x_2m.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_2m=r_x_2m.x_2m
    WHERE  seq_no=r_x_2m.rownum;


  END LOOP;
  --
  
  FOR r_x_2ms2 in (select rownum, x_2ms2, rowid from EOM_MAIN_SCREEN_LAYOUT where x_2ms2 is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_2ms2=null
    where  rowid=r_x_2ms2.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_2ms2=r_x_2ms2.x_2ms2
    WHERE  seq_no=r_x_2ms2.rownum;


  END LOOP;
  --
  
  FOR r_x_2 in (select rownum, x_2, rowid from EOM_MAIN_SCREEN_LAYOUT where x_2 is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_2=null
    where  rowid=r_x_2.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_2=r_x_2.x_2
    WHERE  seq_no=r_x_2.rownum;


  END LOOP;
  --
  
  FOR r_x_2s2p in (select rownum, x_2s2p, rowid from EOM_MAIN_SCREEN_LAYOUT where x_2s2p is not null)
  LOOP
    UPDATE EOM_MAIN_SCREEN_LAYOUT
    set    x_2s2p=null
    where  rowid=r_x_2s2p.rowid;

    update EOM_MAIN_SCREEN_LAYOUT
    set    x_2s2p=r_x_2s2p.x_2s2p
    WHERE  seq_no=r_x_2s2p.rownum;


  END LOOP;
  --

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  --
  
  DELETE EOM_MAIN_SCREEN_LAYOUT where x_inc is null and x_r is null and x_1mm is null;
end;
/


select  * from EOM_MAIN_SCREEN_LAYOUT;