PRO copy_file
    ON_ERROR, 2
    file_in = 'C:\Users\JAY-LAW\Documents\GitHub\inter\input.txt'
    file_out = 'C:\Users\JAY-LAW\Documents\GitHub\inter\output.txt'
    
    IF ~FILE_TEST(file_in) THEN MESSAGE, 'Error: input.txt not found'
    OPENR, lun, file_in, /GET_LUN, ERROR=err
    IF err NE 0 THEN MESSAGE, 'Error opening input: ' + !ERROR_STATE.MSG
    content = ''
    READF, lun, content
    FREE_LUN, lun
    
    OPENW, lun, file_out, /GET_LUN, ERROR=err
    IF err NE 0 THEN MESSAGE, 'Error opening output: ' + !ERROR_STATE.MSG
    PRINTF, lun, content
    FREE_LUN, lun
    
    PRINT, 'File copied successfully to ' + file_out
END
