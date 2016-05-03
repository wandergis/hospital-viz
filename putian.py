# -*- coding: UTF-8 -*-
import json
hospitals = [
    ["\u4e0a\u6d77",
     "\u4e0a\u6d77\u5e02\u95f5\u884c\u533a\u4e2d\u533b\u9662<br/>\u4e0a\u6d77\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u4e0a\u6d77\u4e07\u4f17\u533b\u9662<br/>\u4e0a\u6d77\u5b89\u771f\u533b\u9662<br/>\u4e0a\u6d77\u798f\u534e\u533b\u9662<br/>\u4e0a\u6d77\u739b\u4e3d\u5973\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u771f\u7231\u5973\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u5fc3\u810f\u75c5\u533b\u9662<br/>\u4e0a\u6d77\u4e94\u5b98\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u8fdc\u5927\u5fc3\u80f8\u533b\u9662<br/>\u4e0a\u6d77\u4ec1\u7231\u533b\u9662<br/>\u4e0a\u6d77\u5929\u5927\u533b\u7597\u7f8e\u5bb9\u533b\u9662<br/>\u4e0a\u6d77\u6caa\u7533\u4e94\u5b98\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u535a\u7231\u533b\u9662<br/>\u4e0a\u6d77\u65b0\u8679\u6865\u533b\u9662<br/>\u4e0a\u6d77\u4e5d\u9f99\u7537\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u57ce\u5e02\u5973\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u897f\u90ca\u9aa8\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u771f\u7f8e\u5987\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u5357\u6d66\u5987\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u8679\u6865\u533b\u9662<br/>\u4e0a\u6d77\u5065\u6865\u533b\u9662<br/>\u4e0a\u6d77\u535a\u7231\u533b\u9662<br/>\u4e0a\u6d77\u957f\u6c5f\u533b\u9662<br/>\u89e3\u653e\u519b411\u533b\u9662<br/>\u4e0a\u6d77\u9633\u5149\u4e2d\u533b\u533b\u9662<br/>\u4e0a\u6d77\u82f1\u6e2f\u6ccc\u5c3f\u5916\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u963f\u6ce2\u7f57\u7537\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u73ab\u7470\u5973\u5b50\u533b\u9662<br/>\u4e0a\u6d77\u5eb7\u65b0\u533b\u9662<br/>\u4e0a\u6d77\u5723\u7231\u533b\u9662<br/>\u4e0a\u6d77\u540c\u5fb7\u533b\u9662<br/>\u4e0a\u6d77\u5b89\u5e73\u533b\u9662<br/>\u6c5f\u4e1c\u6ccc\u5c3f\u5916\u79d1\u533b\u9662<br/>\u4e0a\u6d77\u4e5d\u5dde\u6ccc\u5c3f\u533b\u9662<br/>\u4e0a\u6d77\u9752\u57ce\u533b\u9662<br/>\u4e0a\u6d77\u535a\u5927\u533b\u9662<br/>\u4e0a\u6d77\u4e2d\u4e9a\u533b\u9662", "38"],
    ["\u5317\u4eac",
     "\u5317\u4eac\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u5317\u4eac\u4fea\u4eba\u5973\u5b50\u533b\u9662<br/>\u5317\u4eac\u5317\u6d77\u533b\u9662<br/>\u5317\u4eac\u524d\u6d77\u80a1\u9aa8\u5934\u533b\u9662<br/>\u5317\u4eac\u5e02\u6167\u6148\u533b\u9662<br/>\u5317\u4eac\u4e94\u6d32\u5973\u5b50\u533b\u9662<br/>\u5317\u4eac\u5723\u4fdd\u7f57\u7537\u5b50\u533b\u9662<br/>\u5317\u4eac\u6052\u5b89\u4e2d\u533b\u9662<br/>\u5317\u4eac\u5efa\u56fd\u533b\u9662<br/>\u5317\u4eac\u56fd\u9645\u533b\u7597\u4e2d\u5fc3<br/>\u5317\u4eac\u5929\u4f26\u4e0d\u5b55\u4e0d\u80b2\u533b\u9662<br/>\u5317\u4eac\u7f8e\u8054\u81e3\u533b\u7597\u7f8e\u5bb9\u533b\u9662<br/>\u5317\u4eac\u6167\u4e2d\u533b\u9662<br/>\u5317\u4eac\u9633\u5149\u4e3d\u4eba\u5987\u79d1\u533b\u9662<br/>\u5317\u4eac\u6052\u5b89\u4e2d\u533b\u9662<br/>\u5317\u4eac\u4eac\u57ce\u76ae\u80a4\u75c5\u533b\u9662<br/>\u5317\u4eac\u4eac\u5317\u533b\u9662<br/>\u5317\u4eac\u745e\u4eac\u7cd6\u5c3f\u75c5\u533b\u9662<br/>\u5317\u4eac\u4f17\u5b89\u5eb7\u4e2d\u533b\u9aa8\u79d1<br/>\u5317\u4eac\u739b\u4e3d\u5987\u5a74\u533b\u9662<br/>\u5317\u4eac\u9ea6\u745e\u9aa8\u79d1\u533b\u9662<br/>\u5317\u4eac\u5065\u5bab\u533b\u9662", "22"],
    ["\u82cf\u5dde",
     "\u82cf\u5dde\u4e1c\u5434\u533b\u9662<br/>\u82cf\u5dde\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u6606\u5c71\u8679\u6865\u533b\u9662<br/>\u5e38\u719f\u4e1c\u65b9\u5987\u79d1\u533b\u9662<br/>\u5e38\u719f\u4ec1\u7231\u533b\u9662<br/>\u6606\u5c71\u9633\u5149\u533b\u9662<br/>\u82cf\u5dde\u5723\u7231\u533b\u9662<br/>\u82cf\u5dde\u65b0\u533b\u79d1", "8"],
    ["\u5929\u6d25",
     "\u5929\u6d25\u5764\u5982\u739b\u4e3d\u533b\u9662<br/>\u5929\u6d25\u534e\u5317\u533b\u9662<br/>\u5929\u6d25\u534e\u53a6\u533b\u9662<br/>\u5929\u6d25\u4e3d\u4eba\u5973\u5b50\u533b\u9662<br/>\u5929\u6d25\u534e\u5c71\u533b\u9662<br/>\u5929\u6d25\u6021\u6cf0\u751f\u6b96\u4e13\u79d1\u533b\u9662<br/>\u5929\u6d25\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u5929\u6d25\u6021\u6cf0\u533b\u9662<br/>\u5929\u6d25\u4e50\u56ed\u533b\u9662<br/>\u5929\u6d25\u957f\u5e9a\u8033\u9f3b\u5589\u533b\u9662", "10"],
    ["\u5e7f\u5dde",
     "\u5e7f\u5dde\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u5e7f\u5dde\u73b0\u4ee3\u533b\u9662<br/>\u5e7f\u5dde\u957f\u5b89\u533b\u9662<br/>\u5e7f\u5dde\u76ca\u5bff\u533b\u9662<br/>\u5e7f\u5dde\u5229\u5fb7\u533b\u9662<br/>\u756a\u79ba\u4e1c\u65b9\u4fea\u4eba\u533b\u9662<br/>\u756a\u79ba\u739b\u8389\u4e9a\u809b\u80a0\u533b\u9662<br/>\u5e7f\u5dde\u5723\u4e9a\u6ccc\u5c3f\u5916\u79d1\u533b\u9662<br/>\u5e7f\u5dde\u5973\u5b50\u533b\u9662<br/>\u5e7f\u5dde\u5e02\u6c5f\u5357\u533b\u9662<br/>\u5e7f\u5dde\u6d4e\u6148\u533b\u9662<br/>\u5e7f\u4e1c\u6c11\u5b89\u533b\u9662<br/>\u5e7f\u5dde\u957f\u6cf0\u533b\u9662<br/>\u5e7f\u5dde\u5065\u5b89\u533b\u9662<br/>\u5e7f\u5dde458\u533b\u9662<br/>\u5e7f\u5dde\u82b1\u90fd\u4eba\u7231\u533b\u9662<br/>\u5e7f\u5dde\u8fdc\u4e1c\u7f8e\u5bb9\u533b\u9662", "17"],
    ["\u73e0\u6d77",
     "\u73e0\u6d77\u60e0\u7231\u533b\u9662<br/>\u73e0\u6d77\u4e5d\u9f99\u533b\u9662<br/>\u73e0\u6d77\u9633\u5149\u533b\u9662", "3"],
    ["\u60e0\u5dde",
     "\u60e0\u5dde\u4ec1\u5fb7\u5987\u79d1\u533b\u9662<br/>\u60e0\u9633\u5973\u5b50\u533b\u9662<br/>\u60e0\u5dde\u4e1c\u6c5f\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662", "3"],
    ["\u4e2d\u5c71",
     "\u4e2d\u5c71\u73b0\u4ee3\u5987\u79d1\u533b\u9662<br/>\u4e2d\u5c71\u5e02\u56fd\u4e39\u4e2d\u533b\u9662<br/>\u4e2d\u5c71\u548c\u5e73\u4e2d\u533b\u9662<br/>\u4e2d\u5c71\u9633\u5149\u533b\u9662", "4"],
    ["\u6c55\u5934", "\u6c55\u5934\u5987\u4ea7\u533b\u9662", "1"],
    ["\u4e1c\u839e",
     "\u4e1c\u839e\u73b0\u4ee3\u5987\u79d1\u533b\u9662<br/>\u5858\u53a6\u5eb7\u6865\u533b\u9662<br/>\u4e1c\u839e\u5e38\u5e73\u533b\u9662<br/>\u4e1c\u839e\u5eb7\u6865\u5987\u79d1\u533b\u9662<br/>\u4e1c\u839e\u4e4c\u6c99\u533b\u9662<br/>\u4e1c\u839e\u4e07\u798f\u5987\u4ea7\u533b\u9662<br/>\u4e1c\u839e\u5357\u534e\u5987\u79d1\u533b\u9662<br/>\u4e1c\u839e\u4e1c\u65b9\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662", "8"],
    ["\u6c5f\u95e8",
     "\u6c5f\u95e8\u739b\u4e3d\u5987\u79d1\u533b\u9662<br/>\u6c5f\u95e8\u798f\u5eb7\u533b\u9662", "2"],
    ["\u8087\u5e86", "\u8087\u5e86\u798f\u5eb7\u533b\u9662", "1"],
    ["\u4f5b\u5c71",
     "\u4f5b\u5c71\u4e09\u6c34\u5973\u5b50\u533b\u9662<br/>\u987a\u5fb7\u5e7f\u6d4e\u4e2d\u533b\u9662<br/>\u987a\u5fb7\u65b0\u4e16\u7eaa\u6ccc\u5c3f\u533b\u9662<br/>\u987a\u5fb7\u5e84\u5934\u533b\u9662<br/>\u987a\u5fb7\u9633\u5149\u5eb7\u590d\u533b\u9662", "5"],
    ["\u6df1\u5733",
     "\u6df1\u5733\u7f8e\u83b1\u7f8e\u5bb9\u533b\u9662<br/>\u6df1\u5733\u798f\u534e\u4e2d\u897f\u533b\u7ed3\u5408\u533b\u9662<br/>\u6df1\u5733\u535a\u7231\u533b\u9662<br/>\u6df1\u5733\u66d9\u5149\u533b\u9662<br/>\u6df1\u5733\u8fdc\u4e1c\u5987\u513f\u79d1\u533b\u9662<br/>\u6df1\u5733\u4ec1\u7231\u533b\u9662<br/>\u6df1\u5733\u548c\u7f8e\u5987\u513f\u79d1\u533b\u9662<br/>\u6df1\u5733\u4ec1\u5eb7\u533b\u9662<br/>\u6df1\u5733\u7f57\u5c97\u533b\u9662<br/>\u6df1\u5733\u96ea\u8c61\u533b\u9662<br/>\u6df1\u5733\u5065\u5b89\u533b\u9662<br/>\u6df1\u5733\u534e\u5357\u5987\u79d1\u533b\u9662<br/>\u6df1\u5733\u56fd\u745e\u6ccc\u5c3f\u5916\u79d1\u533b\u9662<br/>\u6df1\u5733\u97e9\u7f8e\u533b\u7597\u7f8e\u5bb9\u533b\u9662<br/>\u6df1\u5733\u5065\u4e30\u533b\u9662<br/>\u6df1\u5733\u9f99\u6d4e\u533b\u9662<br/>\u6df1\u5733\u540c\u4ec1\u5987\u79d1\u533b\u9662<br/>\u6df1\u5733\u51e4\u51f0\u533b\u9662<br/>\u6df1\u5733\u9633\u5149\u533b\u9662", "19"],
    ["\u6606\u660e",
     "\u6606\u660e\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u4e91\u5357\u739b\u8389\u4e9a\u5973\u5b50\u533b\u9662<br/>\u4e91\u5357\u739b\u8389\u4e9a\u533b\u9662<br/>\u6606\u660e\u897f\u660c\u8def\u533b\u9662<br/>\u6606\u660e\u9633\u5149\u533b\u9662<br/>\u6606\u660e\u4ec1\u7231\u533b\u9662<br/>\u6606\u660e\u4e5d\u5dde\u533b\u9662<br/>\u89e3\u653e\u519b478\u533b\u9662\u5987\u4ea7\u4e2d\u5fc3<br/>\u6606\u660e\u4e5d\u5dde\u6ccc\u5c3f\u533b\u9662", "9"],
    ["\u7389\u6eaa", "\u7389\u6eaa\u4e5d\u5dde\u533b\u9662", "1"],
    ["\u66f2\u9756",
     "\u5bcc\u6e90\u9633\u5149\u533b\u9662<br/>\u66f2\u9756\u4e5d\u5dde\u533b\u9662", "2"],
    ["\u91cd\u5e86",
     "\u91cd\u5e86\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u91cd\u5e86\u534e\u5c71\u4e2d\u533b\u4e73\u817a\u75c5\u533b\u9662<br/>\u91cd\u5e86\u5764\u5982\u739b\u4e3d\u533b\u9662<br/>\u91cd\u5e86\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u91cd\u5e86\u90fd\u5e02\u4e3d\u4eba\u533b\u9662<br/>\u91cd\u5e86\u4e07\u5dde\u535a\u751f\u533b\u9662<br/>\u91cd\u5e86\u4e07\u5dde\u7f8e\u5987\u4ea7\u533b\u9662<br/>\u6daa\u9675\u535a\u751f\u548c\u7f8e\u5987\u4ea7\u533b\u9662<br/>\u91cd\u5e86\u5e02\u7231\u5fb7\u534e\u533b\u9662<br/>\u91cd\u5e86\u4e94\u6d32\u5973\u5b50\u533b\u9662<br/>\u7b2c\u4e09\u519b\u533b\u5927\u5b66\u91cd\u5e86\u65b0\u6865\u533b\u9662<br/>\u91cd\u5e86\u9633\u5149\u533b\u9662<br/>\u4e07\u5dde\u9633\u5149\u773c\u79d1\u533b\u9662<br/>\u91cd\u5e86\u7231\u5fb7\u534e\u533b\u9662<br/>\u91cd\u5e86\u751f\u6b96\u5065\u5eb7\u533b\u9662<br/>\u91cd\u5e86\u7ea2\u697c\u533b\u9662<br/>\u89e3\u653e\u519b\u7b2c324\u533b\u9662<br/>\u6daa\u9675\u4e09\u5ce1\u533b\u9662<br/>\u91cd\u5e86\u7ea2\u5341\u5b57\u4f1a\u533b\u9662", "19"],
    ["\u6210\u90fd",
     "\u6210\u90fd\u957f\u5f81\u533b\u9662<br/>\u6210\u90fd\u535a\u7231\u533b\u9662<br/>\u6210\u90fd\u4e3d\u4eba\u5973\u5b50\u533b\u9662<br/>\u6210\u90fd\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u56db\u5ddd\u534e\u7f8e\u7d2b\u99a8\u533b\u5b66\u7f8e\u5bb9\u533b\u9662<br/>\u6210\u90fd\u5b89\u742a\u513f\u5987\u4ea7\u533b\u9662<br/>\u6210\u90fd\u8700\u90fd\u4e73\u817a\u533b\u9662<br/>\u6210\u90fd\u7cd6\u5c3f\u75c5\u4e13\u79d1\u533b\u9662<br/>\u6210\u90fd\u66d9\u5149\u7537\u79d1\u533b\u9662<br/>\u6210\u90fd\u739b\u5229\u4e9a\u5987\u4ea7\u533b\u9662<br/>\u6210\u90fd\u6b27\u4e9a\u7537\u79d1\u533b\u9662<br/>\u56db\u5ddd\u9633\u5149\u5987\u79d1\u533b\u9662<br/>\u6210\u90fd\u5eb7\u65b0\u5987\u79d1\u533b\u9662<br/>\u6210\u90fd\u6d4e\u6c11\u5973\u5b50\u533b\u9662<br/>\u6210\u90fd\u7cd6\u5c3f\u75c5\u4e13\u79d1\u533b\u9662<br/>\u6210\u90fd\u66d9\u5149\u7537\u79d1\u533b\u9662", "16"],
    ["\u96c5\u5b89",
     "\u89e3\u653e\u519b\u7b2c\u4e09\u5341\u4e03\u533b\u9662", "1"],
    ["\u9075\u4e49", "\u9075\u4e49\u5973\u5b50\u533b\u9662", "1"],
    ["\u51c9\u5c71",
     "\u51c9\u5c71\u5987\u4ea7\u533b\u9662<br/>\u51c9\u5c71\u7537\u79d1\u533b\u9662", "2"],
    ["\u5357\u5145", "\u5357\u5145\u89e3\u653e\u519b51\u533b\u9662", "1"],
    ["\u4e50\u5c71",
     "\u6b66\u8b66\u56db\u5ddd\u603b\u961f\u533b\u9662", "1"],
    ["\u798f\u5dde",
     "\u798f\u5dde\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u798f\u5dde\u9f13\u697c\u533b\u9662<br/>\u798f\u5dde\u73b0\u4ee3\u5987\u4ea7\u533b\u9662<br/>\u798f\u5dde\u5de6\u6d77\u533b\u9662<br/>\u798f\u5dde\u603b\u533b\u9662\u7b2c\u4e8c\u9644\u5c5e\u533b\u9662<br/>\u798f\u6e05\u9633\u5149\u5973\u5b50\u533b\u9662<br/>\u798f\u5dde\u4e1c\u5357\u5973\u5b50\u533b\u9662<br/>\u798f\u5dde\u798f\u5174\u5987\u4ea7\u533b\u9662<br/>\u798f\u5dde\u8a89\u76db\u533b\u9662", "9"],
    ["\u821f\u5c71",
     "\u821f\u5c71\u73b0\u4ee3\u5987\u79d1\u533b\u9662<br/>\u821f\u5c71\u5e02\u5343\u5c9b\u533b\u9662<br/>\u821f\u5c71\u5e02\u5343\u5c9b\u533b\u9662\u5987\u4ea7\u79d1", "3"],
    ["\u53a6\u95e8",
     "\u53a6\u95e8\u767b\u7279\u53e3\u8154\u533b\u9662<br/>\u53a6\u95e8\u53cb\u597d\u5987\u79d1<br/>\u53a6\u95e8\u6e56\u91cc\u5eb7\u4e50\u95e8\u8bca\u90e8", "3"],
    ["\u8386\u7530",
     "\u8386\u7530\u4e3d\u4eba\u5987\u79d1\u533b\u9662<br/>\u8386\u7530\u76db\u5174\u533b\u9662<br/>\u8386\u7530\u4e2d\u897f\u533b\u809b\u80a0\u533b\u9662", "3"],
    ["\u5b81\u6ce2",
     "\u5b81\u6ce2\u7f8e\u83b1\u6574\u5f62\u7f8e\u5bb9\u533b\u9662<br/>\u5b81\u6ce2\u535a\u7231\u533b\u9662<br/>\u5b81\u6ce2\u8679\u6865\u533b\u9662<br/>\u5b81\u6ce2\u6b27\u4e9a\u7537\u79d1\u533b\u9662<br/>\u5b81\u6ce2\u752c\u57ce\u533b\u9662<br/>\u6148\u6eaa\u5723\u7231\u533b\u9662", "6"],
    ["\u676d\u5dde",
     "\u676d\u5dde\u65b0\u4e1c\u65b9\u5987\u4ea7\u79d1\u533b\u9662<br/>\u676d\u5dde\u739b\u8389\u4e9a\u5987\u5973\u533b\u9662<br/>\u676d\u5dde\u8679\u6865\u533b\u9662<br/>\u676d\u5dde\u5efa\u56fd\u533b\u9662<br/>\u676d\u5dde\u5929\u76ee\u5c71\u533b\u9662<br/>\u676d\u5dde\u8427\u5c71\u4e5d\u9f99\u7537\u79d1\u533b\u9662<br/>\u676d\u5dde\u5e7f\u4ec1\u533b\u9662<br/>\u676d\u5dde\u963f\u6ce2\u7f57\u7537\u5b50\u533b\u9662<br/>\u676d\u5dde\u548c\u7766\u533b\u9662<br/>\u676d\u5dde\u548c\u7766\u533b\u9662<br/>\u676d\u5dde\u771f\u7231\u533b\u9662", "11"],
    ["\u6e56\u5dde",
     "\u6e56\u5dde\u9633\u5149\u5973\u5b50\u533b\u9662", "1"],
    ["\u6cc9\u5dde",
     "\u6cc9\u5dde\u534e\u7f8e\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u6cc9\u5dde\u5357\u4e9a\u534e\u4fa8\u533b\u9662<br/>\u6cc9\u5dde\u65b0\u9633\u5149\u5973\u5b50\u533b\u9662<br/>\u6cc9\u5dde\u5764\u5982\u739b\u4e3d\u533b\u9662<br/>\u6cc9\u5dde\u5357\u4e9a\u533b\u9662", "5"],
    ["\u91d1\u534e",
     "\u6d59\u6c5f\u91d1\u534e\u535a\u5eb7\u751f\u6b96\u533b\u9662<br/>\u6d59\u6c5f\u91d1\u534e\u535a\u5eb7\u751f\u6b96\u533b\u9662", "2"],
    ["\u5609\u5174",
     "\u6d59\u6c5f\u65b0\u5b89\u56fd\u9645\u533b\u9662<br/>\u5609\u5174\u66d9\u5149\u4e2d\u897f\u533b\u7ed3\u5408\u533b\u9662<br/>\u5609\u5174\u535a\u7231\u533b\u9662<br/>\u5609\u5174\u66d9\u5149\u4e2d\u897f\u533b\u7ed3\u5408\u533b\u9662", "4"],
    ["\u53f0\u5dde", "\u6e29\u5cad\u548c\u5e73\u533b\u9662", "1"],
    ["\u6e29\u5dde",
     "\u745e\u5b89\u534e\u4e1c\u533b\u9662<br/>\u6e29\u5dde\u957f\u5f81\u533b\u9662<br/>\u6e29\u5dde\u534f\u548c\u533b\u9662<br/>\u6e29\u5dde\u5efa\u56fd\u533b\u9662<br/>\u6e29\u5dde\u7ea2\u65d7\u533b\u9662<br/>\u6e29\u5dde\u7231\u5c14\u4e94\u5b98\u79d1\u533b\u9662", "6"],
    ["\u9f99\u5ca9",
     "\u9f99\u5ca9\u5973\u5b50\u533b\u9662<br/>\u9f99\u5ca9\u9633\u5149\u533b\u9662", "2"],
    ["\u6d4e\u5357",
     "\u6d4e\u5357\u7f8e\u83b1\u6574\u5f62\u533b\u9662<br/>\u6d4e\u5357\u4e73\u817a\u533b\u9662<br/>\u6d4e\u5357\u5764\u5982\u739b\u4e3d\u533b\u9662<br/>\u6d4e\u5357\u534e\u590f\u533b\u9662<br/>\u89e3\u653e\u519b\u7b2c\u4e09\u4e03\u4e00\u4e2d\u5fc3\u533b\u9662<br/>\u6d4e\u5357\u6574\u5f62\u7f8e\u5bb9\u533b\u9662<br/>\u6d4e\u5357\u5987\u79d1\u533b\u9662<br/>\u5c71\u4e1c\u7ea2\u5341\u5b57\u4f1a\u533b\u9662<br/>\u6d4e\u5357\u9aa8\u79d1\u533b\u9662<br/>\u6d4e\u5357\u9633\u5149\u5973\u5b50\u533b\u9662", "10"],
    ["\u6f4d\u574a",
     "\u6f4d\u574a\u535a\u7231\u533b\u9662<br/>\u6f4d\u574a\u957f\u5b89\u533b\u9662<br/>\u6f4d\u574a\u548c\u5e73\u533b\u9662", "3"],
    ["\u9752\u5c9b",
     "\u9752\u5c9b\u5987\u5a74\u533b\u9662<br/>\u9752\u5c9b\u739b\u4e3d\u5987\u4ea7\u533b\u9662<br/>\u9752\u5c9b\u957f\u5f81\u9662<br/>\u9752\u5c9b\u66d9\u5149\u7537\u79d1\u533b\u9662<br/>\u5c71\u4e1c\u9752\u5c9b\u66d9\u5149\u533b\u9662<br/>\u9752\u5c9b\u96c6\u7f8e\u6574\u5f62\u7f8e\u5bb9\u533b\u9662<br/>\u9752\u5c9b\u65b0\u9633\u5149\u533b\u9662", "7"],
    ["\u5fb7\u5dde", "\u9f50\u6cb3\u9633\u5149\u533b\u9662", "1"],
    ["\u5a01\u6d77",
     "\u5a01\u6d77\u73b0\u4ee3\u5973\u5b50\u533b\u9662", "1"],
    ["\u804a\u57ce",
     "\u804a\u57ce\u4e1c\u660c\u5e9c\u4e09\u533b\u9662", "1"],
    ["\u6dc4\u535a",
     "\u5c71\u4e1c\u6dc4\u535a\u91d1\u76fe\u533b\u9662<br/>\u6dc4\u535a\u5973\u5b50\u533b\u9662", "2"],
    ["\u54c8\u5c14\u6ee8",
     "\u9ed1\u9f99\u6c5f\u739b\u4e3d\u4e9a\u5987\u4ea7\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u4e1c\u5317\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u548c\u5e73\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u548c\u7f8e\u5987\u4ea7\u533b\u9662<br/>\u54c8\u5c14\u6ee8\u5e02\u751f\u6b96\u4fdd\u5065\u4e2d\u5fc3\u9662<br/>\u54c8\u5c14\u6ee8\u6b27\u4e9a\u7537\u79d1\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u957f\u5e9a\u8033\u9f3b\u5589\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u9633\u5149\u5973\u5b50\u533b\u9662<br/>\u9ed1\u9f99\u6c5f\u7701\u6b66\u8b66\u9ec4\u91d1\u533b\u9662\u5987\u79d1", "9"],
    ["\u957f\u6625",
     "\u957f\u6625\u540c\u6d4e\u533b\u9662<br/>\u5409\u6797\u603b\u961f\u533b\u9662<br/>\u957f\u6625\u957f\u5e9a\u8033\u9f3b\u5589\u533b\u9662<br/>\u957f\u6625\u9633\u5149\u5973\u5b50\u533b\u9662<br/>\u957f\u6625\u9633\u5149\u53e3\u8154\u533b\u9662", "5"],
    ["\u56db\u5e73", "\u56db\u5e73\u9633\u5149\u533b\u9662", "1"],
    ["\u5ef6\u8fb9",
     "\u5ef6\u5409\u535a\u751f\u73b0\u4ee3\u5987\u79d1\u533b\u9662", "1"],
    ["\u6c88\u9633",
     "\u6c88\u9633\u5317\u9675\u533b\u9662<br/>\u6c88\u9633\u66d9\u5149\u7537\u79d1\u533b\u9662<br/>\u6b66\u8b66\u8fbd\u5b81\u7701\u603b\u961f\u533b\u9662<br/>\u89e3\u653e\u519b\u6c88\u9633463\u533b\u9662\u5e0c\u7f8e\u6574\u5f62\u7f8e\u5bb9", "4"],
    ["\u5927\u8fde",
     "\u5927\u8fde\u957f\u57ce\u5987\u79d1\u533b\u9662<br/>\u5927\u8fde\u65b0\u4e16\u7eaa\u533b\u9662<br/>\u5927\u8fde\u9633\u5149\u533b\u9662", "3"],
    ["\u65e0\u9521",
     "\u65e0\u9521\u739b\u4e3d\u4e9a\u533b\u9662<br/>\u65e0\u9521\u5609\u4ed5\u6052\u4fe1\u533b\u9662<br/>\u65e0\u9521\u5357\u7ad9\u533b\u9662<br/>\u65e0\u9521\u8679\u6865\u533b\u9662<br/>\u6c5f\u9634\u4e1c\u65b9\u5973\u5b50\u533b\u9662<br/>\u5b9c\u5174\u6b66\u8b66\u533b\u9662<br/>\u6c5f\u9634\u4e5d\u9f99\u6ccc\u5c3f\u5916\u79d1\u533b\u9662<br/>\u65e0\u9521\u65b0\u533a\u533b\u9662", "8"],
    ["\u5357\u4eac",
     "\u6c5f\u82cf\u65bd\u5c14\u7f8e\u6574\u5f62\u7f8e\u5bb9\u533b\u9662<br/>\u5357\u4eac\u66d9\u5149\u533b\u9662<br/>\u5357\u4eac\u6c5f\u5b81\u535a\u7231\u533b\u9662<br/>\u5357\u4eac\u5e02\u6c5f\u5b81\u533a\u4f17\u5f69\u95e8\u8bca\u90e8<br/>\u5357\u4eac\u4e16\u7eaa\u73b0\u4ee3\u5987\u4ea7\u533b\u9662\uff08\u5357\u9662\u3001\u4e1c\u9662\uff09<br/>\u5357\u4eac\u5efa\u56fd\u7537\u79d1\u533b\u9662<br/>\u5357\u4eac\u5eb7\u8c6a\u5987\u79d1<br/>\u5357\u4eac\u9633\u5149\u80bf\u7624\u533b\u9662", "8"],
    ["\u5f20\u5bb6\u6e2f",
     "\u5f20\u5bb6\u6e2f\u671d\u9633\u4e94\u5b98\u79d1\u533b\u9662", "1"],
    ["\u6cf0\u5dde",
     "\u6c5f\u82cf\u6cf0\u5dde\u7ea2\u623f\u5b50\u533b\u9662<br/>\u6cf0\u5dde\u5e02\u6d77\u9675\u533b\u9662<br/>\u6cf0\u5dde\u6d77\u9675\u5973\u5b50\u533b\u9662", "3"],
    ["\u76d0\u57ce",
     "\u76d0\u57ce\u534f\u548c\u5eb7\u590d\u533b\u9662", "1"],
    ["\u5bbf\u8fc1",
     "\u5bbf\u8fc1\u5e02\u5987\u4ea7\u533b\u9662<br/>\u6cd7\u6d2a\u9633\u5149\u513f\u7ae5\u533b\u9662", "2"],
    ["\u6dee\u5b89",
     "\u6c5f\u82cf\u6dee\u5b89\u4e2d\u5c71\u533b\u9662<br/>\u6dee\u5b89\u4e2d\u5c71\u533b\u9662<br/>\u6dee\u5b89\u751f\u6b96\u533b\u9662", "3"],
    ["\u5357\u901a",
     "\u6c5f\u82cf\u6d77\u5b89\u534e\u5c71\u533b\u9662<br/>\u5357\u901a\u548c\u7f8e\u5bb6\u5987\u4ea7\u79d1\u533b\u9662<br/>\u5357\u901a\u957f\u57ce\u533b\u9662", "3"],
    ["\u6b66\u6c49",
     "\u6b66\u6c49\u534e\u590f\u533b\u9662<br/>\u6b66\u6c49\u534e\u7f8e\u533b\u9662<br/>\u6b66\u6c49\u73b0\u4ee3\u5973\u5b50\u5987\u79d1\u533b\u9662<br/>\u6b66\u6c49\u5f53\u4ee3\u4f73\u4e3d\u533b\u9662<br/>\u6e56\u5317\u8363\u519b\u533b\u9662<br/>\u6b66\u6c49\u9633\u5149\u5973\u5b50\u533b\u9662<br/>\u6b66\u6c49\u534e\u4ec1\u533b\u9662", "7"],
    ["\u8346\u5dde", "\u8346\u5dde\u534e\u5eb7\u533b\u9662", "1"],
    ["\u9ec4\u5188",
     "\u9ec4\u5188\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662", "1"],
    ["\u9ec4\u77f3",
     "\u6e56\u5317\u9ec4\u77f3\u798f\u5eb7\u533b\u9662", "1"],
    ["\u8944\u9633",
     "\u8944\u9633\u5e02\u7b2c\u4e94\u4eba\u6c11\u533b\u9662", "1"],
    ["\u4e4c\u6d77", "\u4e4c\u6d77\u73b0\u4ee3\u533b\u9662", "1"],
    ["\u547c\u548c\u6d69\u7279",
     "\u5185\u8499\u53e4\u5929\u9a84\u533b\u9662<br/>\u547c\u548c\u6d69\u7279\u4e94\u6d32\u5973\u5b50\u533b\u9662", "2"],
    ["\u8d35\u9633",
     "\u8d35\u5dde\u9000\u4f11\u533b\u5e08\u533b\u9662<br/>\u8d35\u9633\u4e94\u5b98\u4e2d\u5fc3<br/>\u8d35\u9633\u957f\u6c5f\u533b\u9662<br/>\u8d35\u9633\u548c\u8c10\u9633\u5149\u533b\u9662<br/>\u8d35\u9633\u9a6c\u738b\u5e99\u533b\u9662<br/>\u8d35\u9633\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u8d35\u9633\u548c\u7f8e\u5987\u4ea7\u533b\u9662", "7"],
    ["\u94dc\u4ec1", "\u94dc\u4ec1\u534e\u590f\u533b\u9662", "1"],
    ["\u5b89\u987a",
     "\u5b89\u987a\u9633\u5149\u5987\u79d1\u533b\u9662", "1"],
    ["\u6bd5\u8282", "\u6bd5\u8282\u73b0\u4ee3\u533b\u9662", "1"],
    ["\u957f\u6c99",
     "\u957f\u6c99\u534e\u590f\u533b\u9662<br/>\u957f\u6c99\u6e58\u6c5f\u533b\u9662\u4e03\u5927\u533b\u9662<br/>\u957f\u6c99\u9633\u5149\u533b\u9662<br/>\u957f\u6c99\u4ec1\u7231\u533b\u9662<br/>\u957f\u6c99\u6052\u751f\u624b\u5916\u79d1\u533b\u9662<br/>\u957f\u6c99\u535a\u5927\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662<br/>\u957f\u6c99\u5357\u65b9\u9aa8\u5916\u79d1\u533b\u9662<br/>\u957f\u6c99\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u957f\u6c99\u4e3d\u4eba\u5987\u4ea7\u533b\u9662<br/>\u957f\u6c99\u9633\u5149\u533b\u9662<br/>\u6b66\u8b66\u6e56\u5357\u7701\u603b\u961f\u533b\u9662", "11"],
    ["\u90f4\u5dde",
     "\u6e56\u5357\u90f4\u5dde\u798f\u5eb7\u533b\u9662", "1"],
    ["\u6e58\u6f6d",
     "\u6e58\u6f6d\u9633\u5149\u773c\u79d1\u4e2d\u5fc3", "1"],
    ["\u5a04\u5e95", "\u5a04\u5e95\u9633\u5149\u533b\u9662", "1"],
    ["\u5357\u660c",
     "\u5357\u660c\u5e02\u7b2c\u4e94\u533b\u9662<br/>\u5357\u660c\u4ec1\u7231\u5973\u5b50\u533b\u9662<br/>\u5357\u660c\u66d9\u5149\u624b\u8db3\u5916\u79d1\u533b\u9662<br/>\u5357\u660c\u4f73\u7f8e\u7f8e\u5bb9\u533b\u9662<br/>\u5357\u660c\u534e\u5c71\u4e0d\u5b55\u4e0d\u80b2\u533b\u9662<br/>\u5357\u660c\u535a\u7231\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662<br/>\u5357\u660c\u4e1c\u5927\u809b\u80a0\u4e13\u79d1\u533b\u9662<br/>\u5357\u660c\u535a\u5927\u8033\u9f3b\u54bd\u5589\u4e13\u79d1\u533b\u9662<br/>\u5357\u660c\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662<br/>\u5357\u660c\u4ec1\u7231\u5973\u5b50\u533b\u9662", "10"],
    ["\u4e5d\u6c5f",
     "\u4e5d\u6c5f\u739b\u4e3d\u4e9a\u533b\u9662<br/>\u4e5d\u6c5f\u65b0\u4e16\u7eaa\u533b\u9662<br/>\u4e5d\u6c5f\u9633\u5149\u5973\u5b50\u533b\u9662", "3"],
    ["\u5409\u5b89",
     "\u6c5f\u897f\u5409\u5b89\u5e02\u7b2c\u4e8c\u4eba\u6c11\u533b\u9662", "1"],
    ["\u840d\u4e61",
     "\u840d\u4e61\u5e02\u65b0\u4e16\u7eaa\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662<br/>\u840d\u4e61\u5987\u79d1\u533b\u9662", "2"],
    ["\u8d63\u5dde",
     "\u8d63\u5dde\u73b0\u4ee3\u6ccc\u5c3f\u4e13\u79d1\u533b\u9662", "1"],
    ["\u4e0a\u9976",
     "\u4e0a\u9976\u4e1c\u5927\u809b\u80a0\u4e13\u79d1\u533b\u9662<br/>\u4e0a\u9976\u534f\u548c\u533b\u9662", "2"],
    ["\u592a\u539f",
     "\u5c71\u897f\u73b0\u4ee3\u5987\u4ea7\u533b\u9662<br/>\u5c71\u897f\u6c11\u751f\u533b\u9662<br/>\u592a\u539f\u7cd6\u5c3f\u75c5\u4e13\u79d1\u533b\u9662<br/>\u592a\u539f\u65b0\u533b\u533b\u9662<br/>\u592a\u539f\u76ca\u6c11\u4e2d\u533b\u9662<br/>\u6b66\u8b66\u5c71\u897f\u603b\u961f\u533b\u9662<br/>\u5c71\u897f\u957f\u5e9a\u8033\u9f3b\u5589\u533b\u9662<br/>\u592a\u539f\u7cd6\u5c3f\u75c5\u4e13\u79d1\u533b\u9662<br/>\u592a\u539f\u65b0\u533b\u533b\u9662<br/>\u592a\u539f\u76ca\u6c11\u4e2d\u533b\u9662<br/>\u592a\u767d\u765c\u98ce\u533b\u9662", "11"],
    ["\u4e34\u6c7e",
     "\u4e34\u6c7e\u73b0\u4ee3\u5973\u5b50\u533b\u9662", "1"],
    ["\u9633\u6cc9",
     "\u5c71\u897f\u9633\u6cc9\u4e1c\u65b9\u751f\u6b96\u533b\u9662", "1"],
    ["\u957f\u6cbb", "\u957f\u6cbb\u5973\u5b50\u533b\u9662", "1"],
    ["\u5927\u540c",
     "\u5927\u540c\u65b0\u65f6\u4ee3\u5987\u79d1\u533b\u9662", "1"],
    ["\u664b\u57ce",
     "\u664b\u57ce\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u664b\u57ce\u751f\u6b96\u533b\u9662", "2"],
    ["\u664b\u4e2d",
     "\u5c71\u897f\u65b0\u9633\u5149\u5987\u79d1\u533b\u9662", "1"],
    ["\u8fd0\u57ce",
     "\u8fd0\u57ce\u79b9\u90fd\u4eba\u6c11\u533b\u9662<br/>\u8fd0\u57ce\u79b9\u90fd\u4eba\u6c11\u533b\u9662", "2"],
    ["\u897f\u5b89",
     "\u897f\u5b89\u4fea\u4eba\u533b\u9662<br/>\u6b66\u8b66\u9655\u897f\u603b\u961f\u533b\u9662<br/>\u897f\u5b89\u9633\u5149\u533b\u9662", "3"],
    ["\u5305\u5934",
     "\u5305\u5934\u73b0\u4ee3\u5973\u5b50\u5987\u4ea7\u533b\u9662", "1"],
    ["\u868c\u57e0",
     "\u6fb3\u7f8e\u4f73\u5973\u5b50\u533b\u9662<br/>\u868c\u57e0\u89e3\u653e\u519b\u4e00\u4e8c\u4e09\u4e2d\u5fc3\u533b\u9662", "2"],
    ["\u4eb3\u5dde", "\u6da1\u9633\u9633\u5149\u533b\u9662", "1"],
    ["\u829c\u6e56",
     "\u829c\u6e56\u9633\u5149\u773c\u79d1\u533b\u9662<br/>\u829c\u6e56\u4e39\u51e4\u671d\u9633\u5987\u79d1\u533b\u9662", "2"],
    ["\u5de2\u6e56",
     "\u5de2\u6e56\u5eb7\u5e73\u5987\u4ea7\u533b\u9662<br/>\u5de2\u6e56\u9633\u5149\u5987\u5e7c\u533b\u9662", "2"],
    ["\u6dee\u5317",
     "\u6dee\u5317\u5973\u5b50\u533b\u9662<br/>\u6dee\u5317\u9633\u5149\u5fc3\u7406\u9662", "2"],
    ["\u5408\u80a5",
     "\u5408\u80a5\u5e02\u4e2d\u5c71\u533b\u9662<br/>\u5408\u80a5\u4e5d\u9f99\u7537\u79d1\u533b\u9662<br/>\u5408\u80a5\u4e39\u51e4\u671d\u9633\u5987\u79d1\u533b\u9662", "3"],
    ["\u5b89\u9633", "\u5b89\u9633\u534f\u548c\u533b\u9662", "1"],
    ["\u90d1\u5dde",
     "\u6cb3\u5357\u4e2d\u90fd\u76ae\u80a4\u75c5\u533b\u9662<br/>\u6cb3\u5357\u7701\u519b\u533a\u533b\u9662<br/>\u90d1\u5dde\u96c6\u7f8e\u6574\u5f62\u7f8e\u5bb9\u533b\u9662<br/>\u90d1\u5dde\u534e\u590f\u767d\u765c\u98ce\u533b\u9662<br/>\u5de9\u4e49\u9633\u5149\u533b\u9662<br/>\u90d1\u5dde\u534e\u5c71\u533b\u9662", "6"],
    ["\u8bb8\u660c",
     "\u8bb8\u660c\u65b0\u65f6\u4ee3\u5987\u79d1\u533b\u9662<br/>\u8bb8\u660c\u51e4\u51f0\u533b\u9662<br/>\u8bb8\u660c\u4e2d\u5c71\u533b\u9662", "3"],
    ["\u5eca\u574a",
     "\u5eca\u574a\u4e07\u798f\u533b\u9662<br/>\u5eca\u574a\u4e16\u7eaa\u534f\u548c\u533b\u9662", "2"],
    ["\u4fdd\u5b9a",
     "\u4fdd\u5b9a\u4eac\u6d25\u533b\u9662<br/>\u4fdd\u5b9a\u4e16\u7eaa\u534f\u548c\u533b\u9662<br/>\u4fdd\u5b9a\u957f\u5b89\u533b\u9662<br/>\u4fdd\u5b9a\u73b0\u4ee3\u5973\u5b50\u533b\u9662<br/>\u4fdd\u5b9a\u767d\u765c\u98ce\u533b\u9662", "5"],
    ["\u5510\u5c71",
     "\u5510\u5c71\u4eac\u57ce\u76ae\u80a4\u75c5\u533b\u9662<br/>\u5510\u5c71\u5973\u5b50\u533b\u9662<br/>\u5510\u5c71\u7ea2\u5341\u5b57\u533b\u9662", "3"],
    ["\u6d1b\u9633",
     "\u6d1b\u9633\u7261\u4e39\u5973\u5b50\u533b\u9662<br/>\u89e3\u653e\u519b534\u533b\u9662<br/>\u6d1b\u9633\u7261\u4e39\u5973\u5b50\u533b\u9662", "3"],
    ["\u4fe1\u9633",
     "\u4fe1\u9633\u6ccc\u5c3f\u5916\u79d1\u533b\u9662", "1"],
    ["\u5e73\u9876\u5c71",
     "\u5e73\u9876\u5c71\u5e02\u6b66\u8b66\u533b\u9662", "1"],
    ["\u6f2f\u6cb3", "\u6f2f\u6cb3\u4e1c\u65b9\u533b\u9662", "1"],
    ["\u77f3\u5bb6\u5e84",
     "\u6cb3\u5317\u4e1c\u65b9\u4e2d\u897f\u533b\u7ed3\u5408\u533b\u9662<br/>\u77f3\u5bb6\u5e84\u7f8e\u8054\u81e3\u533b\u7597\u7f8e\u5bb9\u533b\u9662", "2"],
    ["\u90af\u90f8",
     "\u90af\u90f8\u4ec1\u7231\u5987\u79d1\u533b\u9662", "1"],
    ["\u62c9\u8428",
     "\u897f\u85cf\u535a\u7231\u533b\u9662<br/>\u62c9\u8428\u5317\u5927\u6ccc\u5c3f\u751f\u6b96\u533b\u9662", "2"],
    ["\u94f6\u5ddd",
     "\u5b81\u590f\u897f\u4eac\u5987\u4ea7\u533b\u9662", "1"],
    ["\u5170\u5dde",
     "\u5170\u5dde\u4ec1\u548c\u533b\u9662<br/>\u5170\u5dde\u4ec1\u548c\u533b\u9662", "2"],
    ["\u6842\u6797",
     "\u5e7f\u897f\u9633\u5149\u533b\u9662<br/>\u6842\u6797\u9633\u5149\u533b\u9662", "2"],
    ["\u67f3\u5dde", "\u67f3\u5dde\u798f\u5eb7\u533b\u9662", "1"],
    ["\u4f0a\u7281",
     "\u4f0a\u7281\u9633\u5149\u5973\u5b50\u533b\u9662", "1"],
    ["\u4f0a\u5b81",
     "\u4f0a\u5b81\u9633\u5149\u5973\u5b50\u533b\u9662", "1"],
    ["\u4e4c\u9c81\u6728\u9f50",
     "\u65b0\u5f4a\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a\u4eba\u6c11\u533b\u9662\u80bf\u7624\u4e2d\u5fc3<br/>\u65b0\u7586\u7231\u5fb7\u534e\u533b\u9662", "2"],
    ["\u6d77\u53e3",
     "\u6b66\u8b66\u6d77\u5357\u603b\u961f\u533b\u9662\u5987\u79d1\u4e2d\u5fc3", "1"]
]
str = {}
for i in hospitals:
    str[i[0].decode('unicode_escape').encode('utf-8')] = {
        "count": i[2].decode('unicode_escape').encode('utf-8'),
        "hospital": i[1].decode('unicode_escape').encode('utf-8').split('<br/>')
    }
print json.dumps(str, ensure_ascii=False)
