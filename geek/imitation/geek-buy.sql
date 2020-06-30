CREATE TABLE `user_t` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`nickname` varchar(64) NULL,
`phone` int(11) NOT NULL,
`password` varchar(255) NOT NULL,
`avatar` varchar(255) NULL,
`gender` varchar(16) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `coupon_t` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`price` decimal(20,2) NULL,
`expire_datetime` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
`desc_info` varchar(255) NULL,
`condition_price` decimal(11,2) NULL,
`use_condition` varchar(255) NULL,
PRIMARY KEY (`id`) 
)
COMMENT = '优惠券
';
CREATE TABLE `user_receiving_address` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`receiver_name` varchar(255) NULL,
`receiver_phone` int(11) NULL,
`receive_zone` varchar(255) NULL,
`detail_address` varchar(255) NULL,
`zipcode` int(6) NULL,
`is_default` tinyint(1) NULL,
`user_id` int(11) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `green_card` (
`id` int(11) NOT NULL,
`card_type` varchar(255) NULL,
`card_duration` int(11) NULL,
`card_price` decimal(10,2) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `cart_t` (
`id` int(11) NOT NULL,
`goods_id` int(11) NULL,
`quantity` int(11) NULL,
`user_id` int(11) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `order_t` (
`id` int(11) NOT NULL,
`order_num` int(11) NULL,
`create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
`pay_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
`total_mount` decimal(20,2) NULL,
`order_status` tinyint(1) NULL,
`cart_id` int(11) NULL,
`user_id` int(11) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `goods_t` (
`id` int(11) NOT NULL,
`goods_img` varchar(128) NULL,
`goods__name` varchar(255) NULL,
`goods_price` decimal(20,2) NULL,
`goods_desc` varchar(255) NULL,
`goods_type` varchar(255) NULL,
`origin_price` decimal(20,2) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `goods_situation` (
`id` int(11) NOT NULL,
`goods_id` int(11) NULL,
`sales_quantity` int(11) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `user_to_coupon` (
`id` int(11) NOT NULL,
`user_id` int(11) NULL,
`coupon_id` int(11) NULL,
`coupon_quantity` int(11) NULL,
PRIMARY KEY (`id`) 
);
CREATE TABLE `user_to_green_card` (
`id` int(11) NOT NULL,
`user_id` int(11) NULL,
`green_card_id` int(11) NULL,
PRIMARY KEY (`id`) 
);
