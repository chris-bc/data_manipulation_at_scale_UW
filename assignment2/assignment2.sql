-- 1a

--select docid=10398_txt_earn from frequency
select count(*) from Frequency where docid='10398_txt_earn';


-- 1b
-- project term (select docid=10398_txt_earn and count=1 from frequency)
select count(distinct(term)) from Frequency where docid='10398_txt_earn' and count=1;

-- 1c
-- project term ( select docid=10398_txt_earn and count=1 from frequency)
-- union
-- project term(docid=925_txt_trade and count=1 from frequency)
select count(*) from (
select distinct(term) from Frequency where docid='10398_txt_earn' and count=1
union
select distinct(term) from Frequency where docid='925_txt_trade' and count=1);

-- 1d
-- select number of unique documents containing 'law' or 'legal'
select count(distinct docid) from Frequency where term='law' or term='legal';

--1e
-- find all documents with more than 300 total terms, including duplicates
--select count(*) from (select docid,sum(count) from Frequency group by docid having sum(count)>300);
-- Not what they want
select count(*) from (select docid,count(term) from frequency group by docid having count(term)>300);

-- 1f
-- Find all documents that contain both terms transactions and world
select count(*) from (
select distinct docid from Frequency where term='transactions'
intersect
select distinct docid from Frequency where term='world');

--2 ... g
-- Compute matrix product A X B where A and B are tables representing
--   sparse matrices (i.e. cols row,column,value)

-- dot product ~ select sum(a.value*b.value) from a,b where a.row_num=0 and b.col_num=0 and a.col_num=b.row_num


-- General form
-- dotProd(row, col) = select sum(a.value*b.value) from a,b where a.row_num=row and b.col_num=col and a.col_num=b.row_num;

-- A, row 0
-- Z(0,0) = A(0) . B(,0)
--Z(0,0 = select sum(a.value*b.value) from a,b where a.row_num=0 and b.col_num=0 and a.col_num=b.row_num

-- Z(0,1) = A(0) . B(,1)
--Z(0,1) = select sum(a.value*b.value) from a,b where a.row_num=0 and b.col_num=1 and a.col_num=b.row_num

-- Compute A(2,3)
select sum(a.value*b.value) from a,b where a.row_num=2 and b.col_num=3 and a.col_num=b.row_num;

-- W00t - Matrix product
select a.row_num,b.col_num,sum(a.value*b.value) from a,b where a.col_num=b.row_num group by a.row_num,b.col_num;

-- h. Similarity matrix.
-- Compute DDt
select * from (
select a.docid doc_a,b.docid doc_b,sum(a.count*b.count) raw_similarity from frequency a,frequency b where a.term=b.term and a.docid<b.docid group by a.docid,b.docid) where doc_a='10080_txt_crude' and doc_b='17035_txt_earn';

-- i. keyword search
-- Find the best matching document to the keyword query "washington takes treasure"
create view query_freq as select * from frequency union
select 'q' as docid,'washington' as term,1 as count union
select 'q' as docid,'taxes' as term,1 as count union
select 'q' as docid,'treasure' as term,1 as count;

select a.docid doc_a,b.docid doc_b,sum(a.count*b.count) raw_similarity from query_freq a,query_freq b where a.term=b.term and a.docid='q' and b.docid!='q' group by a.docid,b.docid order by raw_similarity desc;