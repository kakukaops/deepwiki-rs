; 定义
(function_item name: (identifier) @definition.function)
(struct_item name: (type_identifier) @definition.class)
(trait_item name: (type_identifier) @definition.interface)
(impl_item type: (type_identifier) @reference.extends) ; impl block 视为关联

; 调用
(call_expression function: (identifier) @reference.call)
(call_expression function: (field_expression field: (field_identifier) @reference.call))
; 宏调用
(macro_invocation macro: (identifier) @reference.call)
(use_declaration) @reference.import