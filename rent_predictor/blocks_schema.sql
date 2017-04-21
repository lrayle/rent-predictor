--  schema for block variables table and way to copy data

DROP TABLE IF EXISTS block_vars;
CREATE TABLE block_vars
    (
    id integer primary key autoincrement,
    varname1 int, -- fill these in. 
    varname2 real
    );

-- copy data
COPY block_vars(id,varname1,varname2)
    FROM 'path/to/ba_block_small.csv'
    DELIMITERS ',' CSV HEADER;