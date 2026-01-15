; 定义
(function_definition
  declarator: (function_declarator
    declarator: (identifier) @definition.function
  )
)
(struct_specifier name: (type_identifier) @definition.class)

; 调用
(call_expression function: (identifier) @reference.call)