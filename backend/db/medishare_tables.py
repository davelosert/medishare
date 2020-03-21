TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `lastname` varchar(50) NOT NULL,"
    "  `firstname` varchar(50) NOT NULL,"
    "  `mail_address` varchar(50) NOT NULL,"
    "  `phone_number` varchar(50) NOT NULL,"
    "  `password` varchar(50) NOT NULL,"
    "  `medical_practice_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`user_id`)"
    ") ENGINE=InnoDB")
TABLES['medical_practices'] = (
    "CREATE TABLE `medical_practices` ("
    "  `medical_practice_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `lanr` char(9) NOT NULL,"
    "  `location_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`medical_practice_id`)"
    ") ENGINE=InnoDB")
TABLES['locations'] = (
    "CREATE TABLE `locations` ("
    "  `location_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `plz` char(5) NOT NULL,"
    "  `place_name` varchar(100),"
    "  PRIMARY KEY (`location_id`)"
    ") ENGINE=InnoDB")
TABLES['advertisements'] = (
    "CREATE TABLE `advertisements` ("
    "  `advertisement_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `advertisement_topic` varchar(100) NOT NULL,"
    "  `advertisement_content` text NOT NULL,"
    "  `number_of_items` int(11) NOT NULL,"
    "  `desired_date` datetime NOT NULL,"
    "  `advertisement_category_id` int(11) NOT NULL,"
    "  `advertisement_status_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`advertisement_id`)"
    ") ENGINE=InnoDB")
TABLES['advertisement_categories'] = (
    "CREATE TABLE `advertisement_categories` ("
    "  `advertisement_category_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `advertisement_category_name` varchar(5) NOT NULL,"
    "  PRIMARY KEY (`advertisement_category_id`)"
    ") ENGINE=InnoDB")
TABLES['advertisement_status'] = (
    "CREATE TABLE `advertisement_status` ("
    "  `advertisement_status_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `advertisement_status_name` int(11) NOT NULL,"
    "  PRIMARY KEY (`advertisement_status_id`)"
    ") ENGINE=InnoDB")
