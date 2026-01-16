; 继承 JS 基础
(function_declaration name: (identifier) @definition.function)
(class_declaration name: (type_identifier) @definition.class)
(interface_declaration name: (type_identifier) @definition.interface)
(method_definition name: (property_identifier) @definition.method)

; 继承与实现
(class_heritage (extends_clause (type_identifier) @reference.extends))
(class_heritage (implements_clause (type_identifier) @reference.extends))

; 调用
(call_expression function: (identifier) @reference.call)
(call_expression function: (member_expression property: (property_identifier) @reference.call))
(import_statement source: (string) @reference.import)
