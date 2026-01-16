; 定义
(function_declaration name: (identifier) @definition.function)
(method_declaration name: (field_identifier) @definition.method)
(type_declaration (type_spec name: (type_identifier) @definition.class)) ; Go struct 视为 class

; 组合 (模拟继承)
(field_declaration type: (type_identifier) @reference.extends) 

; 调用
(call_expression function: (identifier) @reference.call)
(call_expression function: (selector_expression field: (field_identifier) @reference.call))

; ... (原有内容) ...
(import_spec path: (string_literal) @reference.import)

; ... (原有内容) ...
(preproc_include path: (_) @reference.import)
