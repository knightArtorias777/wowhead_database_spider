-- 装备表 初级设计1.0
CREATE TABLE equip_info (
    item_id VARCHAR(64) PRIMARY KEY,     -- 专用的物品ID作为主键
    name VARCHAR(128) NOT NULL,           -- 装备名称，长度 128 足够 eg.
    role_level SMALLINT,                  -- 职业等级，使用 SMALLINT 存储更高效 eg.80
    item_level SMALLINT,                  -- 装备等级 eg.639
    inventory_slot VARCHAR(64),           -- 背包栏位，通常不需要过长的长度 eg.一共16个栏位14个装备
    equip_set VARCHAR(64),                -- 装备套装，长度 64 足够
    equip_subclass varchar(256),        -- 装备子类型
    source VARCHAR(128),                  -- 装备来源
    profession VARCHAR(128)              -- 职业类型
);
CREATE INDEX idx_name ON equip_info(name);
CREATE INDEX idx_item_id ON equip_info(item_id);

--装备内具体细节信息
CREATE TABLE equip_subclass(
    item_id VARCHAR(64) PRIMARY KEY,     --主键
    green_font VARCHAR(128),             --绿字属性
    arms_class VARCHAR(3),               --护甲类型
    primary_attribute varchar(128),      --主属性
    bear_attribute varchar(128),          --耐力属性
    weapon_class varchar(128),            --武器类型
    equid_special varchar(128),            --装备特殊效果 可有可无
    FOREIGN KEY (item_id) REFERENCES equip_info(item_id)
);