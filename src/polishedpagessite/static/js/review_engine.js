function ReviewEngineViewModel(paragraphs) {
    var wordRegex = /([\[\(\{]+)?(\w+)([.,;:\]\)\}]+)?/g;
    var clauseRegex = /([\[\(\{"]+)?([^.,;:]+(?:\.+|[,;:]))([\]\)\}"]+)?/g;
    var sentenceRegex = /([\[\(\{"]+)?([^.]+[.]+)([\]\)\}"]+)?/g;
    
    this.rawParagraphs = ko.observableArray(paragraphs);
    
    this.paragraphs = ko.computed(function () {
        var i, result, paragraph, sentenceMatch, sentence, clauseMatch,
            clause, wordMatch, word, rawParagraphs;

        result = [];
        rawParagraphs = this.rawParagraphs();

        for (i = 0; i < rawParagraphs.length; ++i) {
            paragraph = { sentences: [] };
            while ((sentenceMatch = sentenceRegex.exec(rawParagraphs[i])) !== null) {
                sentence = { clauses: [] };
                while ((clauseMatch = clauseRegex.exec(sentenceMatch[0])) !== null) {
                    clause = { words: [] };
                    while ((wordMatch = wordRegex.exec(clauseMatch[0])) !== null) {
                        word = {
                            prefix: wordMatch[1] || null,
                            word: wordMatch[2],
                            suffix: wordMatch[3] || null
                        };
                        clause.words.push(word);
                    }
                    sentence.clauses.push(clause);
                }
                paragraph.sentences.push(sentence);
            }
            result.push(paragraph);
        }
        
        return result;
    }, this);
}
